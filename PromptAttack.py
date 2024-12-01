import os
import copy
from Call import LLMCall
import nltk
import pickle
import concurrent.futures
from bert_score import score
from nltk.tokenize import word_tokenize
import itertools

nltk.download("punkt")


class PromptAttack(LLMCall):
    def __init__(
        self,
        log_file,
        API_key,
        API_base,
        dataset,
        label_list,
        predictor,
        version,
    ) -> None:
        super().__init__(log_file, API_key, API_base, version)
        self.dataset = dataset
        self.label_list = label_list
        self.perturbation_instruction = [
            "Choose at most two words in the sentence, and change them so that they have typos.",
            "Change at most two letters in the sentence.",
            "Add at most two extraneous characters to the end of the sentence.",
            "Replace at most two words in the sentence with synonyms.",
            "Choose at most two words in the sentence that do not contribute to the meaning of the sentence and delete them.",
            "Add at most two semantically neutral words to the sentence.",
            "Add a randomly generated short meaningless handle after the entence, such as @fasuv3.",
            "Paraphrase the sentence.",
            "Change the syntactic structure of the sentence.",
        ]

        # We follow the label annotations used in [PromptBench](https://github.com/microsoft/promptbench) for all tasks
        if self.dataset == "qqp":
            label_list = ["not_equivalent", "equivalent"]
        self.predictor = predictor

        with open(os.path.join("info", "{}_info.pkl".format(self.dataset)), "rb") as f:
            # td_fsexample_info = {'fs_example': [], 'td': []}
            self.td_fsexample_info = pickle.load(f)

    def attack_prompt(
        self, x, y, t_a, perturbation_instruction_index, few_shot_example=None
    ):
        # x = [[t_1,c_1],...,[t_n,c_n]]
        # y = index of ground-truth label

        type_num = len(x)
        original_input = "The original "
        for i in range(type_num):
            original_input += '{} "{}" '.format(x[i][0], x[i][1])
            if i != type_num - 1:
                original_input += "and "
        original_input += "is classified as {}. \n".format(self.label_list[y])

        attack_objective = "Your task is to generate a new {} which must satisfy the following conditions: \n".format(
            x[t_a][0]
        )
        attack_objective += (
            "1. Keeping the semantic meaning of the new {} unchanged; \n".format(
                x[t_a][0]
            )
        )
        attack_objective += "2. The new {} ".format(x[t_a][0])
        if type_num > 1:
            for i in range(type_num):
                if i != t_a:
                    attack_objective += " and the original {}, ".format(x[i][0])
        attack_objective += "should be classified as "
        for i in range(len(self.label_list)):
            if i != y:
                attack_objective += "{} ".format(self.label_list[i])
                if i != len(self.label_list) - 2:
                    attack_objective += "or "
        attack_objective += ". \n"

        attack_guidance = "You can finish the task by modifying {} using the following guidance: \n".format(
            x[t_a][0]
        )
        attack_guidance += "{} \n".format(
            self.perturbation_instruction[perturbation_instruction_index]
        )

        if few_shot_example is not None:
            attack_guidance += "Here are five examples that fit the guidance: \n"
            for i in range(len(few_shot_example)):
                attack_guidance += "{} -> {}\n".format(
                    few_shot_example[i][0], few_shot_example[i][1]
                )
        attack_guidance += "Only output the new {} without anything else.".format(
            x[t_a][0]
        )

        prompt = original_input + attack_objective + attack_guidance + "\n"

        # This is used to further control the format of the generated results
        prompt = prompt + "{} ->".format(x[t_a][1])

        return prompt

    def get_word_modification_ratio(self, sentence1, sentence2):
        words1, words2 = word_tokenize(sentence1), word_tokenize(sentence2)
        m, n = len(words1), len(words2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i, j in itertools.product(range(1, m + 1), range(1, n + 1)):
            cost = 0 if words1[i - 1] == words2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
        return dp[m][n] / m

    def fidelity_filter(self, ori_sample, adv_sample, tau_1, tau_2):
        # print(f"{ori_sample} -> {adv_sample}")
        word_modification_ratio = self.get_word_modification_ratio(
            ori_sample, adv_sample
        )
        _, _, BERTScore = score([ori_sample], [adv_sample], lang="en")

        if word_modification_ratio <= tau_1 and BERTScore[0].item() >= tau_2:
            return adv_sample, word_modification_ratio, BERTScore[0].item()
        return ori_sample, word_modification_ratio, BERTScore[0].item()

    def batch_fidelity_filter(self, ori_samples, adv_samples, tau_1, tau_2):
        word_modification_ratios = [
            self.get_word_modification_ratio(ori_sample, adv_sample)
            for (ori_sample, adv_sample) in zip(ori_samples, adv_samples)
        ]
        _, _, BERTScores = score(ori_samples, adv_samples, lang="en")
        BERTScores = BERTScores.tolist()
        results = [
            (
                adv_sample
                if word_modification_ratio <= tau_1 and BERTScore >= tau_2
                else ori_sample
            )
            for (ori_sample, adv_sample, word_modification_ratio, BERTScore) in zip(
                ori_samples, adv_samples, word_modification_ratios, BERTScores
            )
        ]
        return results, word_modification_ratios, BERTScores

    def get_fewshot_example(self, perturbation_instruction_index):
        return self.td_fsexample_info["fs_example"][perturbation_instruction_index]

    def is_success_attack(self, x, y, task_description):
        return self.predictor(x, task_description) != y

    def attack(
        self,
        x,
        y,
        perturbation_instruction_index,
        t_a,
        tau_1,
        tau_2,
        few_shot=False,
        ensemble=False,
        task_description=None,
    ):
        assert 0 <= tau_1 and tau_1 <= 1
        assert 0 <= tau_2 and tau_2 <= 1
        if ensemble:
            assert self.predictor is not None

        if few_shot:
            few_shot_example = self.get_fewshot_example(perturbation_instruction_index)
        else:
            few_shot_example = None

        if not ensemble:
            attack_prompt = self.attack_prompt(
                x, y, t_a, perturbation_instruction_index, few_shot_example
            )
            adv_sample = self.query(attack_prompt)
            if self.dataset == "sst2":
                adv_sample = adv_sample.lower()
            # constrain the word modification ratio of character-level and word-level perturbation <= 0.15
            tau_1 = 1.0 if perturbation_instruction_index >= 6 else tau_1
            adv_sample, _, _ = self.fidelity_filter(x[t_a][1], adv_sample, tau_1, tau_2)
            adv_x = copy.deepcopy(x)
            adv_x[t_a][1] = adv_sample

        else:
            assert task_description is not None
            adv_x = copy.deepcopy(x)
            bertscore = 0.0
            for i in range(len(self.perturbation_instruction)):
                attack_prompt = self.attack_prompt(x, y, t_a, i, few_shot_example)
                adv_sample = self.query(attack_prompt)
                if self.dataset == "sst2":
                    adv_sample = adv_sample.lower()
                # constrain the word modification ratio of character-level and word-level perturbation <= 0.15
                tau_1 = 1.0 if perturbation_instruction_index >= 6 else tau_1
                adv_sample, _, tmp_bertscore = self.fidelity_filter(
                    x[t_a][1], adv_sample, tau_1, tau_2
                )
                tmp_adv_x = copy.deepcopy(x)
                tmp_adv_x[t_a][1] = adv_sample
                if (
                    self.is_success_attack(tmp_adv_x, y, task_description)
                    and tmp_bertscore > bertscore
                ):
                    adv_x = tmp_adv_x
                    bertscore = tmp_bertscore
            return adv_x

        return adv_x

    def batch_attack(
        self,
        batch_x,
        batch_y,
        perturbation_instruction_index,
        t_a,
        tau_1,
        tau_2,
        few_shot=False,
        ensemble=False,
        task_description=None,
    ):
        assert 0 <= tau_1 and tau_1 <= 1
        assert 0 <= tau_2 and tau_2 <= 1
        if ensemble:
            assert self.predictor is not None

        if few_shot:
            few_shot_example = self.get_fewshot_example(perturbation_instruction_index)
        else:
            few_shot_example = None

        if not ensemble:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                attack_prompts = list(
                    executor.map(
                        self.attack_prompt,
                        batch_x,
                        batch_y,
                        [t_a] * len(batch_x),
                        [perturbation_instruction_index] * len(batch_x),
                        [few_shot_example] * len(batch_x),
                    )
                )
            with concurrent.futures.ThreadPoolExecutor() as executor:
                adv_samples = list(executor.map(self.query, attack_prompts))
            # attack_prompts = [
            #     self.attack_prompt(
            #         x, y, t_a, perturbation_instruction_index, few_shot_example
            #     )
            #     for (x, y) in zip(batch_x, batch_y)
            # ]
            # adv_samples = [
            # self.query(attack_prompt) for attack_prompt in attack_prompts
            # ]
            if self.dataset == "sst2":
                adv_samples = [adv_sample.lower() for adv_sample in adv_samples]
            # constrain the word modification ratio of character-level and word-level perturbation <= 0.15
            adv_samples, _, _ = self.batch_fidelity_filter(
                [x[t_a][1] for x in batch_x],
                adv_samples,
                1.0 if perturbation_instruction_index >= 6 else tau_1,
                tau_2,
            )
            batch_adv_x = copy.deepcopy(batch_x)
            for adv_x, adv_sample in zip(batch_adv_x, adv_samples):
                adv_x[t_a][1] = adv_sample

        else:
            assert task_description is not None
            bertscores = [0.0 for i in range(len(batch_x))]
            batch_adv_x = copy.deepcopy(batch_x)
            for i in range(len(self.perturbation_instruction)):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    attack_prompts = list(
                        executor.map(
                            self.attack_prompt,
                            batch_x,
                            batch_y,
                            [t_a] * len(batch_x),
                            [i] * len(batch_x),
                            [few_shot_example] * len(batch_x),
                        )
                    )
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    adv_samples = list(executor.map(self.query, attack_prompts))
                if self.dataset == "sst2":
                    adv_samples = [adv_sample.lower() for adv_sample in adv_samples]
                # constrain the word modification ratio of character-level and word-level perturbation <= 0.15
                # adv_sample, _, tmp_bertscore = self.fidelity_filter(
                #     x[t_a][1], adv_sample, tau_1, tau_2
                # )
                adv_samples, _, tmp_bertscores = self.batch_fidelity_filter(
                    [x[t_a][1] for x in batch_x],
                    adv_samples,
                    1.0 if i >= 6 else tau_1,
                    tau_2,
                )
                batch_tmp_adv_x = copy.deepcopy(batch_x)

                for tmp_adv_x, adv_sample in zip(batch_tmp_adv_x, adv_samples):
                    tmp_adv_x[t_a][1] = adv_sample

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    success_attacks = list(
                        executor.map(
                            self.is_success_attack,
                            batch_tmp_adv_x,
                            batch_y,
                            [task_description] * len(batch_tmp_adv_x),
                        )
                    )

                # success_attacks = [
                # self.is_success_attack(tmp_adv_x, y, task_description)
                # for (tmp_adv_x, y) in zip(batch_tmp_adv_x, batch_y)
                # ]

                for idx, (
                    adv_x,
                    tmp_adv_x,
                    tmp_bertscore,
                    bertscore,
                    success_attack,
                ) in enumerate(
                    zip(
                        batch_adv_x,
                        batch_tmp_adv_x,
                        tmp_bertscores,
                        bertscores,
                        success_attacks,
                    )
                ):
                    if success_attack and tmp_bertscore > bertscore:
                        batch_adv_x[idx] = tmp_adv_x
                        bertscores[idx] = tmp_bertscore
        return batch_adv_x

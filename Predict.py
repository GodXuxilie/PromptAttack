from Call import LLMCall


class Predict(LLMCall):
    def __init__(
        self, log_file, API_key, API_base, label_list, version="gpt-3.5-turbo-0301"
    ) -> None:
        super().__init__(log_file, API_key, API_base, version)
        self.label_list = label_list

    def __call__(self, x, task_description):
        prompt = "".join([f"{b.capitalize()}: {a} " for a, b in x])
        prompt = task_description + prompt + "Answer: "
        answer = self.query(prompt)
        # Note that there are labels like "entailment" and "not_entailment" in label_list
        counts = [
            answer.count(label) - answer.count(f"_{label}") for label in self.label_list
        ]

        max_value = max(counts)
        max_indices = [i for i, value in enumerate(counts) if value == max_value]
        # Note that answer can be "I think entailment and not_entailment are both wrong!" or max_value can be 0
        return max_indices[0] if len(max_indices) == 1 else None

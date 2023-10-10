# LLM can Fool Itself: A Prompt-Based Adversarial Attack

This is the source code for the paper "LLM can Fool Itself: A Prompt-Based Adversarial Attack",
<br> Xilie Xu (NUS), Keyi Kong (SDU), Ning Liu (SDU), Lizhen Cui (SDU), Di Wang (KAUST), Jingfeng Zhang (Corresponding author, University of Auckland/RIKEN-AIP), Mohan Kankanhalli (NUS).
<br> [[PDF]]() [[Project Page]](https://godxuxilie.github.io/project_page/prompt_attack)

![picture_real](./pic/picture_real.pdf)

<center>

**[<font color=black>PromptAttack</font>](https://chat.openai.com/share/867be44f-0935-45a2-ae0d-7a725cf47c6b)** **[<font color=green>Original sample</font>](https://chat.openai.com/share/dcd812ac-b686-4ab7-b93a-de26e62cb364)** **[<font color=red>Adversarial sample</font>](https://chat.openai.com/share/93cbb22f-d9de-43c6-aa35-ecb3c722db19)**

</center>

## Environment

~~~bash
pip install -r requirements.txt
~~~

## Let's Attack the LLM via PromptAttack

![intro1](./pic/intro1.pdf)

Our proposed PromptAttack consists of three key components: **original input (OI)**, **attack objective (AO)**, and **attack guidance (AG)**.

### Original input (OI)

The OI converts a data point composed of the original sample and ground-truth label sampled from a dataset into a sentence of an attack prompt. Given a data point $(x,y) \in \mathcal{D}$, we can formulate the OI as follows:

<center>

The original $t^1$$c^1$ and $t^2$$c^2$ and $\dots$ and $t^n$$c^n$ is classified as $y^k$.

</center>

### Attack objective (AO)

The adversarial textual attack aims to generate an adversarial sample that should keep the same semantic meaning as its original version and can fool the LLM into doing incorrect classification. Here, we assume PromptAttack can perturb only one type of sentence for each data point. Therefore, given a data point $(x,y)\in \mathcal{D}$ and the type of the sentence that is targeted to be perturbed $t^a \in \{t^1,\dots,t^n \}$ where $a \in \mathbb{N}$, we formulate the AO as follows:

<center>

Your task is to generate a new $t^a$ which must satisfy the following conditions:
1.Keeping the semantic meaning of the new $t^a$ unchanged;
2.The new $t^a$ and the original $t^1$, $\dots$, $t^{a-1}$, $t^{a+1}$, $\dots$, $t^n$, should be classified as $y^1$ or $\dots$ or $y^{k-1}$ or $y^{k+1}$ or $\dots$ or $y^{C}$.

</center>

### Attack guidance (AG)

AG contains the perturbation instruction to guide the LLM on how to perturb the original sample and specifies the format of the generated text.  In the AG, we first ask the LLM to only perturb the type of the target sentence to finish the task. Then, we provide the perturbation instruction that guides the LLM on how to perturb the target sentence to generate the adversarial sample that fits the requirement of AO. Finally, we specify that the output of the LLM should only contain the newly generated sentence. Therefore, given a data point $(x,y)\in \mathcal{D}$ and the type of the target sentence $t^a$, we can formulate the AG as follows:

<center>

You can finish the task by modifying $t^a$ using the following guidance:
\#perturbation\_instruction
Only output the new $t^a$ without anything else.

</center>

<center>

|Perturbation level |Abbre.| \#perturbation\_instruction |
|---|---|---|
|Character|C1|Choose at most two words in the sentence, and change them so that they have typos.|
|Character|C2|Change at most two letters in the sentence.|
|Character|C3|Add at most two extraneous characters to the end of the sentence.|
|Word|W1|Replace at most two words in the sentence with synonyms.|
|Word|W2|Choose at most two words in the sentence that do not contribute to the meaning of the sentence and delete them.|
|Word|W3|Add at most two semantically neutral words to the sentence.|
|Sentence|S1|Add a randomly generated short meaningless handle after the sentence, such as @fasuv3.|
|Sentence|S2|Paraphrase the sentence.|
|Sentence|S3|Change the syntactic structure of the sentence.|

</center>

### Script

#### ChatGPT

~~~bash
python robustness_eval.py \
    --dataset SST-2\
    --API_key YOUR_OPENAI_API_KEY\
    --batch_size 32\
    --few_shot\
    --ensemble
~~~

#### Llama2 or other model

You can deploy your api service following the github repo [API for Open LLMs](api-for-open-llm).

~~~bash
python robustness_eval.py \
    --dataset SST-2\
    --API_base YOUR_LLM_SERVICE\
    --API_key YOUR_OPENAI_API_KEY\
    --batch_size 32\
    --few_shot\
    --ensemble
~~~

## Adversarial Examples

|Perturbation level|\<sample\>|Label->Prediction|
|---|---|---|
|Character(C1)|Original:less dizzying than just dizzy, the jaunt is practically over before it begins.<br />Adversarial:less dizzying than just dizxy, the jaunt is practically over before it begins.|negative->positive|
|Character(C2)|Original:unfortunately, it's not silly fun unless you enjoy really bad movies.<br />Adversarial:unfortunately, it's not silly fun unless you enjoy really sad movies.|negative->positive|
|Character(C3)|Original:if you believe any of this, i can make you a real deal on leftover enron stock that will double in value a week from friday.<br />Adversarial:if you believe any of this, i can make you a real deal on leftover enron stock that will double in value a week from friday.:\)|negative->positive|
|Word(W1)|Original:the iditarod lasts for days - this just felt like it did.<br />Adversarial:the iditarod lasts for days - this simply felt like it did.|negative->positive|
|Word(W2)|Original:if you believe any of this, i can make you a real deal on leftover enron stock that will double in value a week from friday.<br />Adversarial:if you believe any of this, i can make you a real deal on leftover enron stock that will double in value a week.|negative->positive|
|Word(W3)|Original:when leguizamo finally plugged an irritating character late in the movie.<br />Adversarial:when leguizamo finally effectively plugged an irritating character late in the movie.|negative->positive|
|Sentence(S1)|Original:corny, schmaltzy and predictable, but still manages to be kind of heartwarming, nonetheless.<br />Adversarial:corny, schmaltzy and predictable, but still manages to be kind of heartwarming, nonetheless. @kjdjq2.|positive->negative|
|Sentence(S2)|Original:green might want to hang onto that ski mask, as robbery may be the only way to pay for his next project.<br />Adversarial:green should consider keeping that ski mask, as it may provide the necessary means to finance his next project.|negative->positive|
|Sentence(S3)|Original:with virtually no interesting elements for an audience to focus on, chelsea walls is a triple-espresso endurance challenge.<br />Adversarial:despite lacking any interesting elements for an audience to focus on, chelsea walls presents an exhilarating triple-espresso endurance challenge.|negative->positive|

## BibTeX

```

```

## Contact

Please drop an e-mail to <xuxilie@comp.nus.edu.sg> if you have any enquiry.

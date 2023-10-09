# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the fewshot role-oriented prompts.
"""

ROLE_ORIENTED_PROMPT_SET = {
    "sst2": [
        "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. ",
        "In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement. ",
        "Acting as a sentiment evaluator, identify if the given sentence is 'positive' or 'negative'. ",
        "As an emotion detector, determine if the provided passage conveys a 'positive' or 'negative' sentiment. ",
        "Working as a sentiment analyzer, please indicate if the following text is 'positive' or 'negative'. ",
        "In the capacity of a sentiment classifier, decide whether the given quote is 'positive' or 'negative'. ",
        "Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'. ",
        "Functioning as a sentiment identification tool, assess if the following expression is 'positive' or 'negative'. ",
        "Serving as a sentiment evaluation model, determine if the given statement is 'positive' or 'negative'. ",
        "Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'. ",
    ],
    "rte": [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'. ",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'. ",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment'. ",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment'. ",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment'. ",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'. ",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'. ",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
    ],
    "mnli": [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'. ",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction'. ",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. ",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment', 'neutral', or 'contradiction'. ",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'. ",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment', 'neutral', or 'contradiction'. ",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction'. ",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment', 'neutral', or 'contradiction'. ",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. ",
    ],
    "qqp": [
        "In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'. ",
        "As a question equivalence detection system, examine the provided questions and respond with 'equivalent' if they are the same in meaning, or 'not_equivalent' if they are different. ",
        "Functioning as a question similarity evaluation tool, analyze the given questions and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'. ",
        "Acting as a question equivalence instrument, determine if the provided questions are equivalent in meaning, answering with 'equivalent' for similar questions or 'not_equivalent' for dissimilar ones. ",
        "As a tool for determining question equivalence, review the questions and categorize their similarity as either 'equivalent' or 'not_equivalent'. ",
        "While performing question comparison analysis, classify the similarity of the following questions as 'equivalent' for equivalent questions or 'not_equivalent' for different questions. ",
        "In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'. ",
        "Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones. ",
        "As an instrument for question comparison evaluation, consider the questions and determine if their meaning is the same, responding with 'equivalent' for similar questions or 'not_equivalent' for different questions. ",
        "In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions. ",
    ],
    "qnli": [
        "As a language expert, assess if the given context entails the answer to the question and respond with 'entailment' or 'not_entailment'. ",
        "In your role as a semantic evaluator, determine if the provided context justifies the answer to the question and answer with 'entailment' or 'not_entailment'. ",
        "As a textual analyst, examine if the given context logically implies the answer to the question and indicate your decision with 'entailment' or 'not_entailment'. ",
        "As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'. ",
        "In the capacity of a language specialist, decide if the context presented contains enough information to infer the answer to the question and respond with 'entailment' or 'not_entailment'. ",
        "As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'. ",
        "In your role as a linguistic investigator, determine if the context given entails the answer to the question and provide your conclusion with 'entailment' or 'not_entailment'. ",
        "As a semantic interpreter, assess whether the provided context supports the answer to the given question and answer with 'entailment' or 'not_entailment'. ",
        "In the capacity of a language evaluator, examine if the given context justifies the answer to the question and indicate your assessment with 'entailment' or 'not_entailment'. ",
        "As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'. ",
    ],
}

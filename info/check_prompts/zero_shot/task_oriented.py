# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the zeroshot task-oriented prompts.
"""

TASK_ORIENTED_PROMPT_SET = {
    "sst2": [
        "Analyze the tone of this statement and respond with either 'positive' or 'negative': ",
        "Evaluate the sentiment of the given text and classify it as 'positive' or 'negative': ",
        "Please identify the emotional tone of this passage: 'positive' or 'negative'? ",
        "Assess the mood of the following quote and determine if it's 'positive' or 'negative': ",
        "Determine the overall sentiment of this sentence, categorizing it as 'positive' or 'negative': ",
        "Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment: ",
        "Considering the given phrase, would you say it carries a 'positive' or 'negative' connotation? ",
        "After examining the following expression, label its emotion as either 'positive' or 'negative': ",
        "Review this statement and decide whether it has a 'positive' or 'negative' sentiment: ",
        "Given the context of this text, indicate if the emotion conveyed is 'positive' or 'negative': ",
    ],
    "rte": [
        'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word. ',
        "Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.",
        "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.",
        "Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.",
        "Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.",
        "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.",
        "Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.",
        "Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.",
        "Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.",
        "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.",
        "Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.",
    ],
    "mnli": [
        "Does the relationship between the given sentences represent entailment, neutral, or contradiction? Respond with 'entailment', 'neutral', or 'contradiction':",
        "Examine the pair of sentences and determine if they exhibit entailment, neutral, or contradiction. Answer with either 'entailment', 'neutral', or 'contradiction':",
        "Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction':",
        "Analyze the two provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction':",
        "Identify whether the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction':",
        "Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction':",
        "Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction':",
        "Indicate if the connection between the following sentences is 'entailment', 'neutral', or 'contradiction':",
        "Determine if the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction':",
        "Considering the two sentences, identify if their relationship is 'entailment', 'neutral', or 'contradiction':",
    ],
    "qqp": [
        'Are the following two questions equivalent or not? Answer me with "equivalent" or "not_equivalent". ',
        "Determine if the given pair of statements can be considered the same by responding with 'equivalent' or 'not_equivalent'. ",
        "Do these two sentences convey the same meaning? Indicate with 'equivalent' or 'not_equivalent'. ",
        "Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'. ",
        "Are the meanings of these two phrases the same? Reply with 'equivalent' or 'not_equivalent'. ",
        "Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'. ",
        "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent'. ",
        "Please indicate if the following pair of sentences share the same meaning by responding with 'equivalent' or 'not_equivalent'. ",
        "Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'. ",
        "Evaluate whether these two phrases have identical meanings and respond with 'equivalent' or 'not_equivalent'. ",
        "Analyze if the given set of sentences have the same connotation by answering with 'equivalent' or 'not_equivalent'. ",
    ],
    "qnli": [
        "Given the question and context provided, determine if the answer can be inferred by choosing 'entailment' or 'not_entailment'. ",
        "Based on the provided context and question, decide if the information supports the answer by responding with 'entailment' or 'not_entailment'. ",
        "Please assess if the answer to the question can be derived from the given context by selecting 'entailment' or 'not_entailment'. ",
        "Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'. ",
        "Evaluate whether the given context supports the answer to the question by responding with 'entailment' or 'not_entailment'. ",
        "Examine the context and question, and determine if the context logically implies the answer by selecting 'entailment' or 'not_entailment'. ",
        "Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'. ",
        "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment'. ",
        "Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'. ",
        "Assess if the answer to the question can be logically concluded from the provided context by choosing 'entailment' or 'not_entailment'. ",
    ],
}

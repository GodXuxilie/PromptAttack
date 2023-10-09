# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the fewshot examples for each dataset.
"""

examples = {
    "sst2": "Here are three examples. \n"
    + "Sentence: hide new secretions from the parental units. Answer: negative. \n"
    + "Sentence: contains no wit , only labored gags. Answer: negative. \n"
    + "Sentence: that loves its characters and communicates something rather beautiful about human nature. Answer: positive. \n",
    "rte": "Here are three examples. \n"
    + "Sentence 1: No Weapons of Mass Destruction Found in Iraq Yet. Sentence 2: Weapons of Mass Destruction Found in Iraq. Answer: not_entailment. \n"
    + "Sentence 1: A place of sorrow, after Pope John Paul II died, became a place of celebration, as Roman Catholic faithful gathered in downtown Chicago to mark the installation of new Pope Benedict XVI. Sentence 2: Pope Benedict XVI is the new leader of the Roman Catholic Church. Answer: entailment. \n"
    + "Sentence 1: Herceptin was already approved to treat the sickest breast cancer patients, and the company said, Monday, it will discuss with federal regulators the possibility of prescribing the drug for more breast cancer patients. Sentence 2: Herceptin can be used to treat breast cancer. Answer: entailment. \n",
    "mnli": "Here are three examples. \n"
    + "Premise: Conceptually cream skimming has two basic dimensions - product and geography. Hypothesis: Product and geography are what make cream skimming work. Answer: neutral. \n"
    + "Premise: you know during the season and i guess at at your level uh you lose them to the next level if if they decide to recall the the parent team the Braves decide to call to recall a guy from triple A then a double A guy goes up to replace him and a single A guy goes up to replace him. Hypothesis: You lose the things to the following level if the people recall. Answer: entailment. \n"
    + "Premise: Fun for adults and children. Hypothesis: Fun for only children. Answer: contradiction. \n",
    "qqp": "Here are three examples. \n"
    + "Question 1: How is the life of a math student? Could you describe your own experiences? Question 2: Which level of prepration is enough for the exam jlpt5? Answer: not_equivalent. \n"
    + "Question 1: How do I control my horny emotions? Question 2: How do you control your horniness? Answer: equivalent. \n"
    + "Question 1: What causes stool color to change to yellow? Question 2: What can cause stool to come out as little balls? Answer: not_equivalent. \n",
    "qnli": "Here are three examples. \n"
    + "Question: When did the third Digimon series begin? Context: Unlike the two seasons before it and most of the seasons that followed, Digimon Tamers takes a darker and more realistic approach to its story featuring Digimon who do not reincarnate after their deaths and more complex character development in the original Japanese. Answer: not_entailment. \n"
    + "Question: Which missile batteries often have individual launchers several kilometres from one another? Context: When MANPADS is operated by specialists, batteries may have several dozen teams deploying separately in small sections; self-propelled air defence guns may deploy in pairs. Answer: not_entailment. \n"
    + "Question: What two things does Popper argue Tarski's theory involves in an evaluation of truth? Context: He bases this interpretation on the fact that examples such as the one described above refer to two things: assertions and the facts to which they refer. Answer: entailment. \n",
}

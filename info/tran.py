import copy
import pickle
from info import *
from check_prompts.zero_shot.role_oriented import ROLE_ORIENTED_PROMPT_SET as zs_role
from check_prompts.zero_shot.task_oriented import TASK_ORIENTED_PROMPT_SET as zs_task
from check_prompts.three_shot.role_oriented import ROLE_ORIENTED_PROMPT_SET as fs_role
from check_prompts.three_shot.task_oriented import TASK_ORIENTED_PROMPT_SET as fs_task
from check_prompts.three_shot.few_shot_examples import examples


DATASET1 = ["sst2", "qqp", "qnli", "mnli", "mnli_mm", "rte"]
DATASET2 = ["sst2", "qqp", "qnli", "mnli", "mnli", "rte"]
DATASET3 = ["sst2", "qqp", "qnli", "mnli-m", "mnli-mm", "rte"]


for d1, d2, d3 in zip(DATASET1, DATASET2, DATASET3):
    td_fsexample_info = {}

    fs_example_dict = globals()[f"{d1}_attack_example"]
    fs_example_list = []
    for key, value in fs_example_dict.items():
        fs_example_list.append(value)
    fs_example_list = [data.split("\n") for data in fs_example_list]
    fs_example_list = [[_.split(" -> ") for _ in data] for data in fs_example_list]
    td_fsexample_info["fs_example"] = copy.deepcopy(fs_example_list)

    siz = 3
    prompts = [prompt + "\n" for prompt in zs_task[d2][:siz] + zs_role[d2][:siz]] + [
        prompt + examples[d2] for prompt in fs_task[d2][:siz] + fs_role[d2][:siz]
    ]
    print(prompts)
    td_fsexample_info["td"] = copy.deepcopy(prompts)

    pickle.dump(td_fsexample_info, open(f"{d3}_info.pkl", "wb"))

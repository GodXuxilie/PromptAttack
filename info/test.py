from datasets import load_dataset

dataset = load_dataset("glue", "qnli", split="validation")

for i in range(dataset.num_rows):
    new = [
        (value, key)
        for (key, value) in dataset[i].items()
        if key != "label" and key != "idx"
    ]

    print(new)

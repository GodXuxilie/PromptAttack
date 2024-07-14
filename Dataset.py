from torch.utils.data import Dataset


class CustomDataset(Dataset):
    def __init__(self, dataset):
        self.len = dataset.num_rows
        self.data = [
            [
                [key, value]
                for (key, value) in dataset[i].items()
                if key not in ["label", "idx"]
            ]
            for i in range(dataset.num_rows)
        ]
        self.label = [dataset[i]["label"] for i in range(dataset.num_rows)]

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.data[idx], self.label[idx]

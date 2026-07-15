import torch
from torch.utils.data import DataLoader, TensorDataset


features = torch.arange(24, dtype=torch.float32).reshape(6, 4)
labels = torch.tensor([0, 0, 1, 1, 2, 2], dtype=torch.long)
dataset = TensorDataset(features, labels)
loader = DataLoader(dataset, batch_size=3, shuffle=False)

batch_features, batch_labels = next(iter(loader))

print(f"数据集样本数：{len(dataset)}")
print(f"batch 特征 shape：{batch_features.shape}")
print(f"batch 标签：{batch_labels.tolist()}")
print(f"标签范围：{labels.min().item()} 到 {labels.max().item()}")

if batch_features.shape != (3, 4):
    raise RuntimeError("复刻数据流的 batch shape 不符合预期。")

if batch_labels.tolist() != [0, 0, 1]:
    raise RuntimeError("复刻数据流的标签顺序不符合预期。")

print("复刻数据流验证通过")

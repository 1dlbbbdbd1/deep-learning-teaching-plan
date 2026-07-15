import torch
from torch.utils.data import DataLoader, TensorDataset


raw_features = torch.tensor(
    [
        [0.0, 10.0],
        [1.0, 11.0],
        [2.0, 12.0],
        [3.0, 13.0],
    ],
    dtype=torch.float32,
)
labels = torch.tensor([0, 0, 1, 1], dtype=torch.long)

mean = raw_features.mean(dim=0)
std = raw_features.std(dim=0)
normalized_features = (raw_features - mean) / std

dataset = TensorDataset(normalized_features, labels)
loader = DataLoader(dataset, batch_size=2, shuffle=False)
batch_features, batch_labels = next(iter(loader))

print(f"原始特征均值：{mean.tolist()}")
print(f"原始特征标准差：{std.tolist()}")
print(f"标准化后整体均值：{normalized_features.mean().item():.4f}")
print(f"batch 特征 shape：{batch_features.shape}")
print(f"batch 标签 shape：{batch_labels.shape}")

if batch_features.shape != (2, 2):
    raise RuntimeError("batch 特征 shape 不符合预期。")

if batch_labels.shape != (2,):
    raise RuntimeError("batch 标签 shape 不符合预期。")

if abs(normalized_features.mean().item()) > 1e-6:
    raise RuntimeError("标准化后的均值没有接近 0。")

print("Dataset transform normalization 验证通过")

import torch


features = torch.tensor(
    [
        [0.0, 0.1],
        [0.2, 0.3],
        [0.4, 0.5],
        [0.6, 0.7],
        [0.8, 0.9],
        [1.0, 1.1],
    ]
)
labels = torch.tensor([0, 0, 0, 1, 1, 1])

train_features = features[:4]
train_labels = labels[:4]
test_features = features[4:]
test_labels = labels[4:]

print(f"特征矩阵形状：{features.shape}")
print(f"标签形状：{labels.shape}")
print(f"训练集样本数：{len(train_features)}")
print(f"测试集样本数：{len(test_features)}")
print(f"第一条训练特征：{train_features[0].tolist()}")
print(f"第一条训练标签：{train_labels[0].item()}")
print(f"第一条测试特征：{test_features[0].tolist()}")
print(f"第一条测试标签：{test_labels[0].item()}")

if features.shape != (6, 2):
    raise RuntimeError("特征矩阵形状不符合预期。")

if labels.shape != (6,):
    raise RuntimeError("标签形状不符合预期。")

if len(train_features) != 4 or len(test_features) != 2:
    raise RuntimeError("训练集和测试集拆分数量不符合预期。")

print("特征、标签、训练集和测试集验证通过")

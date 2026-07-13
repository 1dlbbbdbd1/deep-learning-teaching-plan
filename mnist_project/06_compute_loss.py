from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 32

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=False,
    transform=transforms.ToTensor(),
)

train_loader = DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=False,
)

images, labels = next(iter(train_loader))

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)

loss_function = nn.CrossEntropyLoss()

scores = model(images)
loss = loss_function(scores, labels)

print(f"模型输出形状：{scores.shape}")
print(f"真实标签形状：{labels.shape}")
print(f"loss 形状：{loss.shape}")
print(f"loss 数值：{loss.item():.4f}")

if scores.shape != (BATCH_SIZE, 10):
    raise RuntimeError("模型输出形状不符合预期。")

if labels.shape != (BATCH_SIZE,):
    raise RuntimeError("真实标签形状不符合预期。")

if loss.dim() != 0:
    raise RuntimeError("loss 应该是一个标量。")

if loss.item() <= 0:
    raise RuntimeError("loss 数值应该大于 0。")

print("损失函数验证通过")

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

with torch.no_grad():
    flat_images = nn.Flatten()(images)
    scores = model(images)

print(f"输入图片 batch 形状：{images.shape}")
print(f"展平后 batch 形状：{flat_images.shape}")
print(f"模型输出形状：{scores.shape}")
print(f"第一张图片的真实标签：{labels[0].item()}")
print(f"第一张图片的 10 个分数：{scores[0].tolist()}")

if flat_images.shape != (BATCH_SIZE, 28 * 28):
    raise RuntimeError("展平后的图片形状不符合预期。")

if scores.shape != (BATCH_SIZE, 10):
    raise RuntimeError("模型输出形状不符合预期。")

print("最小模型前向传播验证通过")

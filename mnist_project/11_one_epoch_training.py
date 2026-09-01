from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 256
LEARNING_RATE = 0.1
RANDOM_SEED = 42
EPOCHS = 1

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

torch.manual_seed(RANDOM_SEED)

train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=transforms.ToTensor(),
)

train_loader = DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=False,
)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

losses = []

for epoch in range(EPOCHS):
    for images, labels in train_loader:
        scores = model(images)
        loss = loss_function(scores, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

batch_count = len(losses)
average_loss = sum(losses) / batch_count
early_average_loss = sum(losses[:20]) / 20
late_average_loss = sum(losses[-20:]) / 20
loss_trend_down = late_average_loss < early_average_loss

print(f"epoch 数：{EPOCHS}")
print(f"训练样本数：{len(train_data)}")
print(f"batch size：{BATCH_SIZE}")
print(f"训练 batch 数：{batch_count}")
print(f"前 20 个 batch 平均 loss：{early_average_loss:.4f}")
print(f"后 20 个 batch 平均 loss：{late_average_loss:.4f}")
print(f"epoch 平均 loss：{average_loss:.4f}")
print(f"一个 epoch 内 loss 是否总体下降：{loss_trend_down}")

if batch_count != len(train_loader):
    raise RuntimeError(f"训练 batch 数不正确：期待 {len(train_loader)}，实际 {batch_count}。")

if average_loss >= 1.0:
    raise RuntimeError(f"epoch 平均 loss 过高：{average_loss:.4f}。")

if not loss_trend_down:
    raise RuntimeError("一个 epoch 结束时，后 20 个 batch 平均 loss 没有低于前 20 个 batch。")

print("完整 epoch 训练验证通过")

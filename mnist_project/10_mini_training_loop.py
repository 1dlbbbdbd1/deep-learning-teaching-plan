from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 32
LEARNING_RATE = 0.1
RANDOM_SEED = 42
MAX_STEPS = 5

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

for step, (images, labels) in enumerate(train_loader, start=1):
    scores = model(images)
    loss = loss_function(scores, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())
    print(f"第 {step} 步 loss：{loss.item():.4f}")

    if step == MAX_STEPS:
        break

loss_decreased = losses[-1] < losses[0]

print(f"训练 batch 数：{len(losses)}")
print(f"第 1 步到第 {MAX_STEPS} 步 loss 是否总体下降：{loss_decreased}")

if len(losses) != MAX_STEPS:
    raise RuntimeError(f"训练步数不正确：期待 {MAX_STEPS}，实际 {len(losses)}。")

if not loss_decreased:
    raise RuntimeError("小训练循环后，最后一步 loss 没有低于第一步。")

print("小训练循环验证通过")

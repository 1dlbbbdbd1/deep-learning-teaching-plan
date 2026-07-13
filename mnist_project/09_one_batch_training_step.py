from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 32
LEARNING_RATE = 0.1
RANDOM_SEED = 42

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

torch.manual_seed(RANDOM_SEED)

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
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

scores_before = model(images)
loss_before = loss_function(scores_before, labels)

optimizer.zero_grad()
loss_before.backward()
optimizer.step()

scores_after = model(images)
loss_after = loss_function(scores_after, labels)

loss_decreased = loss_after.item() < loss_before.item()

print(f"batch size：{BATCH_SIZE}")
print(f"学习率：{LEARNING_RATE}")
print(f"训练前 loss：{loss_before.item():.4f}")
print(f"训练后 loss：{loss_after.item():.4f}")
print(f"同一个 batch 的 loss 是否下降：{loss_decreased}")

if not loss_decreased:
    raise RuntimeError("一次训练步骤后，同一个 batch 的 loss 没有下降。")

print("一次训练步骤验证通过")

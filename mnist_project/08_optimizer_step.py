from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 32
LEARNING_RATE = 0.1

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

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

images, labels = next(iter(train_loader))

linear_layer = nn.Linear(28 * 28, 10)
model = nn.Sequential(
    nn.Flatten(),
    linear_layer,
)

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

weight_before = linear_layer.weight.detach().clone()

scores = model(images)
loss = loss_function(scores, labels)

optimizer.zero_grad()
loss.backward()
optimizer.step()

weight_after = linear_layer.weight.detach()
weight_change = (weight_after - weight_before).norm().item()
weight_changed = weight_change > 0

print(f"学习率：{LEARNING_RATE}")
print(f"loss 数值：{loss.item():.4f}")
print(f"optimizer.step 前后权重是否变化：{weight_changed}")
print(f"权重变化量：{weight_change:.6f}")

if not weight_changed:
    raise RuntimeError("optimizer.step 后权重没有变化。")

print("参数更新验证通过")

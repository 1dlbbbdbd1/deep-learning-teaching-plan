from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 256
LEARNING_RATE = 0.1
RANDOM_SEED = 42
EPOCHS = 1
MIN_EXPECTED_ACCURACY = 85.0

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

torch.manual_seed(RANDOM_SEED)

train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=False,
    transform=transforms.ToTensor(),
)

test_data = datasets.MNIST(
    root=data_dir,
    train=False,
    download=False,
    transform=transforms.ToTensor(),
)

train_loader = DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=False,
)

test_loader = DataLoader(
    dataset=test_data,
    batch_size=BATCH_SIZE,
    shuffle=False,
)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

model.train()
for epoch in range(EPOCHS):
    for images, labels in train_loader:
        scores = model(images)
        loss = loss_function(scores, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

model.eval()
correct_count = 0
total_count = 0

with torch.no_grad():
    for images, labels in test_loader:
        scores = model(images)
        predictions = scores.argmax(dim=1)
        correct_count += (predictions == labels).sum().item()
        total_count += labels.numel()

accuracy = correct_count / total_count * 100

print(f"epoch 数：{EPOCHS}")
print(f"训练样本数：{len(train_data)}")
print(f"测试样本数：{len(test_data)}")
print(f"预测正确数：{correct_count}")
print(f"测试集准确率：{accuracy:.2f}%")

if total_count != len(test_data):
    raise RuntimeError(f"测试样本数不正确：期待 {len(test_data)}，实际 {total_count}。")

if accuracy < MIN_EXPECTED_ACCURACY:
    raise RuntimeError(f"测试集准确率过低：{accuracy:.2f}%。")

print("测试集准确率验证通过")

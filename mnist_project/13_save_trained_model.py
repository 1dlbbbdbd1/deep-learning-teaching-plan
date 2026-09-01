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
models_dir = project_root / "models"
model_path = models_dir / "mnist_linear_state_dict.pt"

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

model.train()
for epoch in range(EPOCHS):
    for images, labels in train_loader:
        scores = model(images)
        loss = loss_function(scores, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

models_dir.mkdir(exist_ok=True)
torch.save(model.state_dict(), model_path)

saved_state_dict = torch.load(model_path, map_location="cpu")
weight_shape = tuple(saved_state_dict["1.weight"].shape)
bias_shape = tuple(saved_state_dict["1.bias"].shape)

print(f"epoch 数：{EPOCHS}")
print(f"训练样本数：{len(train_data)}")
print(f"保存路径：{model_path}")
print(f"模型文件大小：{model_path.stat().st_size} bytes")
print(f"权重形状：{weight_shape}")
print(f"偏置形状：{bias_shape}")

if not model_path.exists():
    raise RuntimeError("模型文件没有保存成功。")

if weight_shape != (10, 784):
    raise RuntimeError(f"权重形状不正确：{weight_shape}。")

if bias_shape != (10,):
    raise RuntimeError(f"偏置形状不正确：{bias_shape}。")

print("模型保存验证通过")

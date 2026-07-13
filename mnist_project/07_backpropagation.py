from pathlib import Path

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

linear_layer = nn.Linear(28 * 28, 10)
model = nn.Sequential(
    nn.Flatten(),
    linear_layer,
)

loss_function = nn.CrossEntropyLoss()

scores = model(images)
loss = loss_function(scores, labels)

print(f"loss 数值：{loss.item():.4f}")
print(f"backward 前梯度：{linear_layer.weight.grad}")

loss.backward()

weight_gradient = linear_layer.weight.grad
bias_gradient = linear_layer.bias.grad

print(f"权重梯度形状：{weight_gradient.shape}")
print(f"偏置梯度形状：{bias_gradient.shape}")
print(f"权重梯度范数：{weight_gradient.norm().item():.4f}")
print(f"偏置梯度范数：{bias_gradient.norm().item():.4f}")

if weight_gradient.shape != (10, 28 * 28):
    raise RuntimeError("权重梯度形状不符合预期。")

if bias_gradient.shape != (10,):
    raise RuntimeError("偏置梯度形状不符合预期。")

if weight_gradient.norm().item() <= 0:
    raise RuntimeError("权重梯度范数应该大于 0。")

print("反向传播验证通过")

import torch
from torch import nn


model = nn.Sequential(
    nn.Conv2d(1, 4, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    nn.Flatten(),
    nn.Linear(4 * 13 * 13, 10),
)

images = torch.randn(2, 1, 28, 28)
logits = model(images)

print(f"输入图片 shape：{images.shape}")
print("模型结构：Conv2d -> ReLU -> MaxPool2d -> Flatten -> Linear")
print(f"输出 logits shape：{logits.shape}")

if logits.shape != (2, 10):
    raise RuntimeError("最小 CNN 输出 shape 不符合预期。")

print("池化和最小 CNN 验证通过")

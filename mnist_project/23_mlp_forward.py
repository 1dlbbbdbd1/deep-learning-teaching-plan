import torch
from torch import nn


BATCH_SIZE = 5

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)

images = torch.randn(BATCH_SIZE, 1, 28, 28)
logits = model(images)

print(f"输入图片 shape：{images.shape}")
print(f"MLP 输出 logits shape：{logits.shape}")
print(f"第一张图片的预测类别：{logits.argmax(dim=1)[0].item()}")

if logits.shape != (BATCH_SIZE, 10):
    raise RuntimeError("MLP 输出 shape 不符合预期。")

print("MLP 前向传播验证通过")

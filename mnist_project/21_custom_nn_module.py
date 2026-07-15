import torch
from torch import nn


class TinyClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.hidden = nn.Linear(28 * 28, 16)
        self.activation = nn.ReLU()
        self.output = nn.Linear(16, 10)

    def forward(self, images):
        x = self.flatten(images)
        x = self.hidden(x)
        x = self.activation(x)
        return self.output(x)


model = TinyClassifier()
images = torch.zeros(3, 1, 28, 28)
logits = model(images)

print(model)
print(f"输入 shape：{images.shape}")
print(f"输出 logits shape：{logits.shape}")

if logits.shape != (3, 10):
    raise RuntimeError("自定义模型输出 shape 不符合预期。")

print("自定义 nn.Module 验证通过")

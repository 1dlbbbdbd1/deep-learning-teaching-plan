import torch
from torch import nn


values = torch.tensor([[-2.0, -0.5, 0.0, 1.0, 3.0]])
relu = nn.ReLU()
activated = relu(values)

print(f"ReLU 前：{values.tolist()}")
print(f"ReLU 后：{activated.tolist()}")
print(f"ReLU 后最小值：{activated.min().item():.1f}")

if activated.min().item() < 0:
    raise RuntimeError("ReLU 后不应该有负数。")

if activated[0, -1].item() != 3.0:
    raise RuntimeError("正数经过 ReLU 后应该保持不变。")

print("激活函数验证通过")

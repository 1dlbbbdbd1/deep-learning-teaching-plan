import torch
from torch import nn


image = torch.zeros(1, 1, 6, 6)
image[:, :, 2:4, 2:4] = 1.0

conv = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=3)
feature_maps = conv(image)

print(f"输入图片 shape：{image.shape}")
print(f"卷积核 shape：{conv.weight.shape}")
print(f"特征图 shape：{feature_maps.shape}")

if feature_maps.shape != (1, 2, 4, 4):
    raise RuntimeError("卷积输出 shape 不符合预期。")

print("卷积和特征图验证通过")

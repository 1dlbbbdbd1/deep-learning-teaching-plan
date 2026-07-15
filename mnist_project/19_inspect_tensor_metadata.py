import torch


images = torch.zeros(4, 1, 28, 28, dtype=torch.float32)
labels = torch.tensor([0, 1, 2, 3], dtype=torch.long)

print(f"图片 shape：{images.shape}")
print(f"图片 dtype：{images.dtype}")
print(f"图片 device：{images.device}")
print(f"标签 shape：{labels.shape}")
print(f"标签 dtype：{labels.dtype}")
print(f"标签 device：{labels.device}")

if images.shape != (4, 1, 28, 28):
    raise RuntimeError("图片 shape 不符合预期。")

if images.dtype != torch.float32:
    raise RuntimeError("图片 dtype 应该是 float32。")

if labels.dtype != torch.long:
    raise RuntimeError("分类标签 dtype 应该是 long。")

if images.device != labels.device:
    raise RuntimeError("图片和标签不在同一个 device。")

print("Tensor 元数据验证通过")

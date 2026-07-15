import torch
from torch import nn


BATCH_SIZE = 2
PATCH_SIZE = 7
EMBED_DIM = 8

images = torch.randn(BATCH_SIZE, 1, 28, 28)
patches = images.unfold(2, PATCH_SIZE, PATCH_SIZE).unfold(3, PATCH_SIZE, PATCH_SIZE)
patches = patches.contiguous().view(BATCH_SIZE, 1, -1, PATCH_SIZE, PATCH_SIZE)
patches = patches.flatten(3).squeeze(1)

projection = nn.Linear(PATCH_SIZE * PATCH_SIZE, EMBED_DIM)
embeddings = projection(patches)

print(f"图片 shape：{images.shape}")
print(f"patch 数量：{patches.shape[1]}")
print(f"patch embedding shape：{embeddings.shape}")

if patches.shape != (BATCH_SIZE, 16, PATCH_SIZE * PATCH_SIZE):
    raise RuntimeError("patch shape 不符合预期。")

if embeddings.shape != (BATCH_SIZE, 16, EMBED_DIM):
    raise RuntimeError("patch embedding shape 不符合预期。")

print("ViT patch embedding 验证通过")

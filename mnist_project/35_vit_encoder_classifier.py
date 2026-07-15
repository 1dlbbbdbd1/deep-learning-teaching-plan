import torch
from torch import nn


torch.manual_seed(42)

BATCH_SIZE = 2
PATCH_COUNT = 16
EMBED_DIM = 8
CLASS_COUNT = 10

patch_embeddings = torch.randn(BATCH_SIZE, PATCH_COUNT, EMBED_DIM)
cls_token = torch.zeros(BATCH_SIZE, 1, EMBED_DIM)
sequence = torch.cat([cls_token, patch_embeddings], dim=1)

encoder_layer = nn.TransformerEncoderLayer(
    d_model=EMBED_DIM,
    nhead=2,
    dim_feedforward=32,
    batch_first=True,
)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=1)
classifier = nn.Linear(EMBED_DIM, CLASS_COUNT)

encoded = encoder(sequence)
cls_output = encoded[:, 0]
logits = classifier(cls_output)

print(f"Transformer 输入 shape：{sequence.shape}")
print(f"CLS 输出 shape：{cls_output.shape}")
print(f"分类 logits shape：{logits.shape}")

if sequence.shape != (BATCH_SIZE, PATCH_COUNT + 1, EMBED_DIM):
    raise RuntimeError("Transformer 输入 shape 不符合预期。")

if logits.shape != (BATCH_SIZE, CLASS_COUNT):
    raise RuntimeError("分类头输出 shape 不符合预期。")

print("ViT Encoder 和分类头验证通过")

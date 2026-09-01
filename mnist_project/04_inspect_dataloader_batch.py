from pathlib import Path

from torch.utils.data import DataLoader
from torchvision import datasets, transforms


BATCH_SIZE = 32

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

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

images, labels = next(iter(train_loader))

print(f"batch size：{BATCH_SIZE}")
print(f"图片 batch 形状：{images.shape}")
print(f"标签 batch 形状：{labels.shape}")
print(f"前 10 个标签：{labels[:10].tolist()}")

if images.shape != (BATCH_SIZE, 1, 28, 28):
    raise RuntimeError("图片 batch 形状不符合预期。")

if labels.shape != (BATCH_SIZE,):
    raise RuntimeError("标签 batch 形状不符合预期。")

print("DataLoader batch 验证通过")

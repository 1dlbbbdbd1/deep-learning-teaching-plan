from pathlib import Path

from torchvision import datasets, transforms


project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

to_tensor = transforms.ToTensor()

train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=to_tensor,
)

image, label = train_data[0]

print(f"训练集样本数：{len(train_data)}")
print(f"第一张图片的标签：{label}")
print(f"图片张量形状：{image.shape}")
print(f"图片张量最小值：{image.min().item():.1f}")
print(f"图片张量最大值：{image.max().item():.1f}")

if image.shape != (1, 28, 28):
    raise RuntimeError("MNIST 图片形状不符合预期。")

if not 0 <= label <= 9:
    raise RuntimeError("MNIST 标签不符合预期。")

print("MNIST 数据验证通过")

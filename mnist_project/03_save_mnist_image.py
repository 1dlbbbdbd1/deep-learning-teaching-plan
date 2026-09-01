from pathlib import Path

from torchvision import datasets


project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"
output_dir = project_root / "outputs"
output_dir.mkdir(exist_ok=True)

train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=True,
)

image, label = train_data[0]
output_path = output_dir / f"mnist_sample_0_label_{label}.png"

image.save(output_path)

relative_path = output_path.relative_to(project_root)
print(f"第一张图片的标签：{label}")
print(f"图片模式：{image.mode}")
print(f"图片尺寸：{image.size}")
print(f"保存图片：{relative_path}")

if label != 5:
    raise RuntimeError("第一张 MNIST 图片标签不符合预期。")

if image.size != (28, 28):
    raise RuntimeError("第一张 MNIST 图片尺寸不符合预期。")

print("MNIST 图片保存验证通过")

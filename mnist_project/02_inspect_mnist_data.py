from pathlib import Path

from torchvision import datasets, transforms


# 当前脚本在 mnist_project/ 目录里。
# parents[1] 表示往上走一层，回到项目根目录。
project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

# ToTensor 会把图片转成 PyTorch Tensor，并把像素缩放到 0.0 到 1.0。
to_tensor = transforms.ToTensor()

# datasets.MNIST 会创建一个 MNIST 数据集对象。
# train=True 表示取训练集；download=True 表示本地没有数据时自动下载。
train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=to_tensor,
)

# train_data[0] 会返回第一条样本。
# 一条样本包含 image 和 label：
# image 是图片 Tensor，label 是这张图片的正确答案。
image, label = train_data[0]

print(f"训练集样本数：{len(train_data)}")
print(f"第一张图片的标签：{label}")
print(f"图片张量形状：{image.shape}")
print(f"图片张量最小值：{image.min().item():.1f}")
print(f"图片张量最大值：{image.max().item():.1f}")

# MNIST 是灰度图，所以形状应该是：
# 1 个颜色通道、28 像素高、28 像素宽。
if image.shape != (1, 28, 28):
    raise RuntimeError("MNIST 图片形状不符合预期。")

# MNIST 是 0 到 9 的数字分类任务，所以标签只能是 0 到 9。
if not 0 <= label <= 9:
    raise RuntimeError("MNIST 标签不符合预期。")

print("MNIST 数据验证通过")

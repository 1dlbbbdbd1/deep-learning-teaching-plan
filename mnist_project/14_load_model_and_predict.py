from pathlib import Path

import torch
from torch import nn
from torchvision import datasets, transforms


SAMPLE_INDEX = 0

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"
model_path = project_root / "models" / "mnist_linear_state_dict.pt"

if not model_path.exists():
    raise FileNotFoundError(
        f"找不到模型文件：{model_path}。请先运行 mnist_project/13_save_trained_model.py。"
    )

test_data = datasets.MNIST(
    root=data_dir,
    train=False,
    download=True,
    transform=transforms.ToTensor(),
)

image, label = test_data[SAMPLE_INDEX]

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)

state_dict = torch.load(model_path, map_location="cpu")
model.load_state_dict(state_dict)
model.eval()

with torch.no_grad():
    single_image_batch = image.unsqueeze(0)
    scores = model(single_image_batch)
    prediction = scores.argmax(dim=1).item()

is_correct = prediction == label

print(f"模型路径：{model_path}")
print(f"样本序号：{SAMPLE_INDEX}")
print(f"图片 batch 形状：{single_image_batch.shape}")
print(f"模型输出形状：{scores.shape}")
print(f"真实标签：{label}")
print(f"预测结果：{prediction}")
print(f"是否预测正确：{is_correct}")

if not is_correct:
    raise RuntimeError(f"预测错误：真实标签 {label}，预测结果 {prediction}。")

print("单张图片预测验证通过")

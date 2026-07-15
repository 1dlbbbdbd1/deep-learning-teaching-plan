import torch
from torch import nn


torch.manual_seed(42)

images = torch.zeros(8, 1, 28, 28)
labels = torch.tensor([0, 1, 0, 1, 0, 1, 0, 1], dtype=torch.long)
images[labels == 0, :, 6:14, 6:14] = 1.0
images[labels == 1, :, 14:22, 14:22] = 1.0

model = nn.Sequential(
    nn.Conv2d(1, 4, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(4 * 13 * 13, 10),
)
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)

with torch.no_grad():
    initial_loss = loss_function(model(images), labels).item()

model.train()
for _ in range(80):
    logits = model(images)
    loss = loss_function(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

model.eval()
with torch.no_grad():
    final_logits = model(images)
    final_loss = loss_function(final_logits, labels).item()
    accuracy = (final_logits.argmax(dim=1) == labels).float().mean().item()

print("任务：用 CNN 区分左上亮块和右下亮块")
print(f"初始 loss：{initial_loss:.4f}")
print(f"最终 loss：{final_loss:.4f}")
print(f"训练集准确率：{accuracy:.2f}")

if final_loss >= initial_loss:
    raise RuntimeError("CNN 训练后 loss 没有下降。")

if accuracy < 0.99:
    raise RuntimeError("CNN 没有学会玩具分类任务。")

print("CNN 玩具训练评估验证通过")

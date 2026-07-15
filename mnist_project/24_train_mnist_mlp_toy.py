import torch
from torch import nn


torch.manual_seed(42)

BATCH_SIZE = 8
TRAINING_STEPS = 120

images = torch.zeros(BATCH_SIZE, 1, 28, 28)
labels = torch.tensor([0, 1, 0, 1, 0, 1, 0, 1], dtype=torch.long)
images[labels == 0, :, 8:20, 4:10] = 1.0
images[labels == 1, :, 8:20, 18:24] = 1.0

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)

with torch.no_grad():
    initial_loss = loss_function(model(images), labels).item()

for _ in range(TRAINING_STEPS):
    logits = model(images)
    loss = loss_function(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    final_logits = model(images)
    final_loss = loss_function(final_logits, labels).item()
    accuracy = (final_logits.argmax(dim=1) == labels).float().mean().item()

print("任务：用 MLP 区分左侧亮块和右侧亮块")
print(f"初始 loss：{initial_loss:.4f}")
print(f"最终 loss：{final_loss:.4f}")
print(f"训练集准确率：{accuracy:.2f}")

if final_loss >= initial_loss:
    raise RuntimeError("MLP 训练后 loss 没有下降。")

if accuracy < 0.99:
    raise RuntimeError("MLP 没有学会玩具分类任务。")

print("MNIST MLP 玩具训练验证通过")

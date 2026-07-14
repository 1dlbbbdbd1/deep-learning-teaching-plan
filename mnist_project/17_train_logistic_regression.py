import torch
from torch import nn


RANDOM_SEED = 42
LEARNING_RATE = 0.2
TRAINING_STEPS = 200

torch.manual_seed(RANDOM_SEED)

features = torch.tensor(
    [
        [-2.0, -1.0],
        [-1.0, -2.0],
        [-2.0, -2.0],
        [1.0, 2.0],
        [2.0, 1.0],
        [2.0, 2.0],
    ]
)
labels = torch.tensor([0, 0, 0, 1, 1, 1])

model = nn.Linear(2, 2)
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

with torch.no_grad():
    initial_logits = model(features)
    initial_loss = loss_function(initial_logits, labels).item()

for _ in range(TRAINING_STEPS):
    logits = model(features)
    loss = loss_function(logits, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    final_logits = model(features)
    final_loss = loss_function(final_logits, labels).item()
    predictions = final_logits.argmax(dim=1)
    accuracy = (predictions == labels).float().mean().item()

print("任务：根据两个特征把样本分成 0 或 1")
print(f"类别数：2")
print(f"训练样本数：{len(features)}")
print(f"训练步数：{TRAINING_STEPS}")
print(f"初始 loss：{initial_loss:.4f}")
print(f"最终 loss：{final_loss:.4f}")
print(f"训练集准确率：{accuracy:.2f}")
print(f"预测结果：{predictions.tolist()}")

if final_loss >= initial_loss:
    raise RuntimeError("训练后 loss 没有下降。")

if accuracy < 0.95:
    raise RuntimeError("训练集准确率低于预期。")

print("逻辑回归训练验证通过")

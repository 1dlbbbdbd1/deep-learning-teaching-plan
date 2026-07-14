import torch
from torch import nn


RANDOM_SEED = 42
LEARNING_RATE = 0.05
TRAINING_STEPS = 300

torch.manual_seed(RANDOM_SEED)

x_train = torch.tensor([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
y_train = 2 * x_train + 1

model = nn.Linear(1, 1)
loss_function = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

with torch.no_grad():
    initial_predictions = model(x_train)
    initial_loss = loss_function(initial_predictions, y_train).item()

for _ in range(TRAINING_STEPS):
    predictions = model(x_train)
    loss = loss_function(predictions, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    final_predictions = model(x_train)
    final_loss = loss_function(final_predictions, y_train).item()
    learned_weight = model.weight.item()
    learned_bias = model.bias.item()

print("训练目标：y = 2 * x + 1")
print(f"训练样本数：{len(x_train)}")
print(f"训练步数：{TRAINING_STEPS}")
print(f"初始 loss：{initial_loss:.4f}")
print(f"最终 loss：{final_loss:.4f}")
print(f"学到的权重 w：{learned_weight:.4f}")
print(f"学到的偏置 b：{learned_bias:.4f}")

if final_loss >= initial_loss:
    raise RuntimeError("训练后 loss 没有下降。")

if abs(learned_weight - 2.0) > 0.2:
    raise RuntimeError("学到的权重离目标 2.0 太远。")

if abs(learned_bias - 1.0) > 0.2:
    raise RuntimeError("学到的偏置离目标 1.0 太远。")

print("线性回归训练验证通过")

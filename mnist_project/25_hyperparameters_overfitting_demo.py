import torch
from torch import nn


def train_with_learning_rate(learning_rate):
    torch.manual_seed(42)
    x = torch.tensor([[-1.0], [0.0], [1.0], [2.0]])
    y = 3 * x - 1
    model = nn.Linear(1, 1)
    loss_function = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    with torch.no_grad():
        initial_loss = loss_function(model(x), y).item()

    for _ in range(80):
        loss = loss_function(model(x), y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        final_loss = loss_function(model(x), y).item()

    return initial_loss, final_loss


slow_initial, slow_final = train_with_learning_rate(0.001)
good_initial, good_final = train_with_learning_rate(0.05)

print(f"小学习率初始 loss：{slow_initial:.4f}")
print(f"小学习率最终 loss：{slow_final:.4f}")
print(f"合适学习率初始 loss：{good_initial:.4f}")
print(f"合适学习率最终 loss：{good_final:.4f}")
print(f"合适学习率是否下降更多：{good_final < slow_final}")

if good_final >= slow_final:
    raise RuntimeError("合适学习率没有比小学习率下降更多。")

print("超参数和过拟合演示验证通过")

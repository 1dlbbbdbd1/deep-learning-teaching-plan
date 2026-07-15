import torch
from torch import nn


torch.manual_seed(42)

features = torch.tensor(
    [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
    ]
)
labels = torch.tensor([0, 1, 1, 0], dtype=torch.long)

model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

before = model[0].weight.detach().clone()

for _ in range(10):
    logits = model(features)
    loss = loss_function(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

after = model[0].weight.detach().clone()
changed = not torch.equal(before, after)

print(f"logits shape：{logits.shape}")
print(f"最终 loss：{loss.item():.4f}")
print(f"参数是否更新：{changed}")

if logits.shape != (4, 2):
    raise RuntimeError("训练闭环输出 shape 不符合预期。")

if not changed:
    raise RuntimeError("参数没有更新。")

print("复刻训练闭环验证通过")

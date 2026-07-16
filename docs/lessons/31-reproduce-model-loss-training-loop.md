# PyTorch MNIST 31 复刻模型、loss 和训练循环

> 核心概念：模型结构、loss、training loop

# 第 31 课：复刻训练闭环

数据流确认后，再复刻模型和训练循环。

顺序是：

```text
模型 forward -> loss -> backward -> optimizer -> eval
```

## 先复刻最小模型

不要一开始就完整搬运复杂项目。先写一个能吃同样 batch、输出同样类别数的最小模型。

## loss 要和任务匹配

分类常用交叉熵。回归常用 MSE。loss 选错，训练会很奇怪。

## 训练循环要逐步确认

每一步都可以打印证据：

- logits shape。
- loss 数值。
- 梯度是否存在。
- 参数是否更新。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\31_reproduce_model_loss_training_loop.py
```

看到 `复刻训练闭环验证通过`，说明你已经验证过 forward、loss、backward 和 step 会让参数更新。

- 写出模型输入输出 shape。
- 跑一个 batch。
- 跑 5 个 batch。
- 跑 1 个 epoch。
- 评估一次。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| training loop | 训练循环，反复做预测、算错、改参数 | `for _ in range(10)` |
| logits | 分类分数 | `logits = model(features)` |
| parameter update | 参数真的被改了 | `changed` |
| reproduction | 复刻，先做最小可运行版本 | 本课目标 |

## 源码逐段讲解

### 1. 准备一个 XOR 风格的小分类任务

```python
features = torch.tensor(
    [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
    ]
)
labels = torch.tensor([0, 1, 1, 0], dtype=torch.long)
```

每条样本有 2 个特征，标签是 0 或 1。

这不是 MNIST，只是一个小到能看懂的训练闭环。

### 2. 定义最小模型

```python
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))
```

输入 2 个特征，输出 2 个类别分数。

中间加 `ReLU`，让模型能处理比直线更复杂的分类边界。

### 3. 训练前复制参数

```python
before = model[0].weight.detach().clone()
```

这行保存训练前第一层权重。后面训练完再比较，确认参数真的变了。

### 4. 跑 10 次训练步骤

```python
for _ in range(10):
    logits = model(features)
    loss = loss_function(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

这就是复刻训练循环时要找的核心骨架：

```text
forward -> loss -> zero_grad -> backward -> step
```

### 5. 检查参数是否更新

```python
changed = not torch.equal(before, after)
```

只看 loss 有时不够。确认参数变化，能帮你排除“忘了 step”这种错误。

## 输出怎么读

- `logits shape：[4, 2]`：4 条样本，每条输出 2 个类别分数。
- `最终 loss`：训练结束时的错误程度。
- `参数是否更新：True`：优化器确实改了模型参数。

## 你真正学到了什么

复刻别人的训练代码时，不要一次搬完整项目。先用最小数据验证四件事：

```text
模型能 forward 吗？
loss 能算吗？
梯度能产生吗？
参数会更新吗？
```

这四件事通过了，再扩大到真实数据和完整 epoch。

## 你可以自己改一改

把：

```python
optimizer.step()
```

临时注释掉，再运行脚本。你会看到 `参数是否更新` 变成 `False` 或检查失败。

这个实验是复刻项目时的救命动作：loss 不动时，先确认参数到底有没有更新。

## Debug 检查

如果 loss 不变，检查是否忘了 `zero_grad()`、`backward()` 或 `optimizer.step()`。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 30 课](30-reproduce-data-pipeline.md)
- 下一课：[第 32 课](32-debug-workflow-practice.md)

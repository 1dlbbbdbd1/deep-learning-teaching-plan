# PyTorch MNIST 10 小训练循环

> 核心概念：for 循环、多 batch 训练

# 第 10 课：把一次训练步骤放进小循环

## 今天只理解一个新东西：for 循环

上一课我们做了一次训练步骤：

```text
猜一次 -> 算 loss -> backward -> step
```

这一课只是把它放进 `for` 循环里，让模型连续看 5 个 batch：

```python
for step, (images, labels) in enumerate(train_loader, start=1):
    scores = model(images)
    loss = loss_function(scores, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

这就是训练循环的雏形。以后完整训练 MNIST，本质上也是这个结构，只是 batch 更多、epoch 更多。

## loss 为什么不一定每一步都下降

你可能会看到类似：

```text
第 1 步 loss：2.2761
第 2 步 loss：2.2427
第 3 步 loss：1.9941
第 4 步 loss：1.8519
第 5 步 loss：1.9844
```

注意第 5 步比第 4 步高了一点，这不奇怪。因为每个 batch 的图片不同，难度也不同。

我们这一课只看一个粗粒度信号：

```text
第 5 步 loss < 第 1 步 loss
```

这说明模型总体在往减少错误的方向走。

## 运行脚本

```powershell
python .\mnist_project\10_mini_training_loop.py
```

期待看到：

```text
训练 batch 数：5
第 1 步到第 5 步 loss 是否总体下降：True
小训练循环验证通过
```

## 本节检查问题

- `for step, (images, labels) in enumerate(...)` 里，`step` 是什么？
- 为什么每个 batch 都要重新 `zero_grad()`？
- 为什么 loss 会波动，而不是每一步都下降？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 9 课](09-one-batch-training-step.md)
- 下一课：[第 11 课](11-one-epoch-training.md)

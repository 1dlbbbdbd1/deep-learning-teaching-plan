# PyTorch MNIST 09 一次完整训练步骤

> 核心概念：forward、loss、zero_grad、backward、step

# 第 9 课：完成一次最小训练步骤

## 今天只理解一件事

训练不是一句神秘咒语，它其实是几句代码按顺序排队：

```python
scores = model(images)
loss = loss_function(scores, labels)
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

可以把它想成：

```text
模型先猜一次 -> 算错多少 -> 清空旧梯度 -> 计算新梯度 -> 更新参数
```

## 为什么还要再算一次 loss

这一课里，我们训练前算一次 loss，更新参数后对同一个 batch 再算一次 loss。

如果训练步骤起作用，通常会看到：

```text
训练后 loss < 训练前 loss
```

这说明模型刚刚往“少错一点”的方向走了一小步。

## 运行脚本

```powershell
python .\mnist_project\09_one_batch_training_step.py
```

期待看到：

```text
训练前 loss：...
训练后 loss：...
同一个 batch 的 loss 是否下降：True
一次训练步骤验证通过
```

## 本节检查问题

- `optimizer.zero_grad()` 为什么要放在 `backward()` 前面？
- `loss.backward()` 和 `optimizer.step()` 谁负责算梯度，谁负责改参数？
- 为什么这节只检查同一个 batch，而不是整个训练集？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 8 课](08-optimizer-step.md)
- 下一课：[第 10 课](10-mini-training-loop.md)

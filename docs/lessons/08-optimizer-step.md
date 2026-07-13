# PyTorch MNIST 08 优化器更新参数

> 核心概念：optimizer、step、learning rate

# 第 8 课：用优化器更新一次参数

## 今天只理解三个词

1. **optimizer**：优化器，负责按梯度修改模型参数。
2. **step**：让优化器真正走一步，也就是更新一次参数。
3. **learning rate**：学习率，控制每一步改多大。

前几课连起来是：

```text
图片 -> 模型 -> loss -> backward 得到梯度
```

这一课多一步：

```text
optimizer.step() -> 参数发生变化
```

## 运行脚本

```powershell
python .\mnist_project\08_optimizer_step.py
```

期待看到：

```text
学习率：0.1
optimizer.step 前后权重是否变化：True
权重变化量：...
参数更新验证通过
```

## 为什么要 zero_grad

PyTorch 默认会累加梯度。训练时通常每一步都先写：

```python
optimizer.zero_grad()
```

意思是：先把上一轮的梯度清掉，再计算这一轮的新梯度。

## 本节检查问题

- `loss.backward()` 和 `optimizer.step()` 分别做什么？
- 学习率太大或太小可能会有什么问题？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 7 课](07-backpropagation.md)
- 下一课：[第 9 课](09-one-batch-training-step.md)

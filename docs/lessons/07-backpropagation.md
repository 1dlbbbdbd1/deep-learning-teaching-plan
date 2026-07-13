# PyTorch MNIST 07 反向传播

> 核心概念：loss.backward、梯度

# 第 7 课：做一次反向传播

## 今天只理解两个词

1. **梯度**：参数应该怎么调整的提示。你可以先理解成“往哪个方向改，loss 可能会变小”。
2. **backward**：从 loss 反向计算梯度的动作。

前面几课连起来是：

```text
图片 -> 模型 -> 分数 -> loss
```

这一课多一步：

```text
loss.backward() -> 参数里出现 grad
```

## 运行脚本

```powershell
python .\mnist_project\07_backpropagation.py
```

期待看到：

```text
backward 前梯度：None
权重梯度形状：torch.Size([10, 784])
偏置梯度形状：torch.Size([10])
反向传播验证通过
```

## 为什么一开始梯度是 None

模型刚创建、刚前向传播时，参数还没有梯度。调用：

```python
loss.backward()
```

之后，PyTorch 会沿着计算图反向计算，给参与计算的参数填上 `.grad`。

## 本节检查问题

- 为什么权重梯度形状是 `[10, 784]`？
- `loss.backward()` 会直接更新参数吗？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 6 课](06-loss-function.md)
- 下一课：[第 8 课](08-optimizer-step.md)

# PyTorch MNIST 07 反向传播

> 核心概念：loss.backward、梯度

# 第 7 课：做一次反向传播

这一课真正要解决的是：

```text
loss 已经算出来了，模型怎么知道每个参数应该往哪个方向改？
```

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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| 参数 | 模型里可以被训练改变的数字 | `linear_layer.weight`、`linear_layer.bias` |
| 梯度 grad | 告诉参数应该怎么改的提示 | `.grad` |
| backward | 从 loss 往回算梯度 | `loss.backward()` |
| 范数 norm | 粗略衡量一堆数字有多大 | `weight_gradient.norm()` |

## 源码逐段讲解

### 1. 把 Linear 层单独拿出来

```python
linear_layer = nn.Linear(28 * 28, 10)
model = nn.Sequential(
    nn.Flatten(),
    linear_layer,
)
```

这里没有直接把 `nn.Linear(...)` 写在 `Sequential` 里，是因为我们后面要查看它的梯度。

`linear_layer.weight` 是权重参数，`linear_layer.bias` 是偏置参数。

### 2. 先算出 loss

```python
scores = model(images)
loss = loss_function(scores, labels)
```

到这里为止，只是完成：

```text
图片 -> 模型 -> 分数 -> loss
```

参数还没有被更新，梯度也还没有算出来。

### 3. backward 前梯度是 None

```python
print(f"backward 前梯度：{linear_layer.weight.grad}")
```

`None` 的意思是：目前还没有梯度。

这不是错误。只是说明我们还没调用 `loss.backward()`。

### 4. 调用 backward

```python
loss.backward()
```

这行会让 PyTorch 沿着刚才的计算过程反着走，计算每个参数对 loss 的影响。

注意：它只计算梯度，不更新参数。

### 5. 查看梯度

```python
weight_gradient = linear_layer.weight.grad
bias_gradient = linear_layer.bias.grad
```

调用 `backward()` 后，参数的 `.grad` 里就会出现梯度。

权重梯度形状是 `[10, 784]`，因为权重本身就是把 784 个输入变成 10 个输出。

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

## 输出怎么读

- `backward 前梯度：None`：还没有算梯度。
- `权重梯度形状：[10, 784]`：每个权重参数都有一个对应梯度。
- `偏置梯度形状：[10]`：每个输出类别有一个偏置梯度。
- `梯度范数`：不是 0，说明确实算出了梯度。

## 你真正学到了什么

`loss.backward()` 的作用是：

```text
根据 loss，计算模型参数的 grad。
```

它不会直接让模型变好。真正改参数的是下一课的优化器。

## 你可以自己改一改

把：

```python
loss.backward()
```

临时注释掉，再运行脚本。你会看到后面拿梯度时出问题。这能帮你确认：梯度不是自动存在的，是 backward 算出来的。

## 本节检查问题

- 为什么权重梯度形状是 `[10, 784]`？
- `loss.backward()` 会直接更新参数吗？
- `.grad` 是模型参数本身，还是参数应该怎么调整的提示？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 6 课](06-loss-function.md)
- 下一课：[第 8 课](08-optimizer-step.md)

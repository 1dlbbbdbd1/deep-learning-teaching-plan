# PyTorch MNIST 08 优化器更新参数

> 核心概念：optimizer、step、learning rate

# 第 8 课：用优化器更新一次参数

这一课真正要解决的是：

```text
梯度已经算出来了，模型参数到底是哪一行代码改掉的？
```

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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| optimizer | 按梯度修改参数的工具 | `torch.optim.SGD(...)` |
| SGD | 一种最基础的优化方法 | `torch.optim.SGD` |
| learning rate | 每次改参数的幅度 | `LEARNING_RATE = 0.1` |
| step | 真正执行一次参数更新 | `optimizer.step()` |
| zero_grad | 清空旧梯度 | `optimizer.zero_grad()` |

## 源码逐段讲解

### 1. 创建优化器

```python
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)
```

`model.parameters()` 把模型里所有可训练参数交给优化器。

`lr=LEARNING_RATE` 告诉优化器每一步改多大。

### 2. 复制更新前的权重

```python
weight_before = linear_layer.weight.detach().clone()
```

这行是为了保存一份“更新前”的权重，后面才能比较参数有没有变化。

`clone()` 可以理解成复制一份。

### 3. 训练三步

```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

这三行顺序很重要：

1. 清空旧梯度。
2. 根据当前 loss 计算新梯度。
3. 用优化器根据梯度更新参数。

### 4. 比较权重变化

```python
weight_change = (weight_after - weight_before).norm().item()
```

如果变化量大于 0，说明参数确实被 `optimizer.step()` 改了。

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

## 输出怎么读

- `学习率：0.1`：本次参数更新步子大小。
- `loss 数值`：更新前这一批样本的错误程度。
- `权重是否变化：True`：优化器确实改了参数。
- `权重变化量`：变化有多大。

## 你真正学到了什么

反向传播和优化器分工不同：

```text
loss.backward()：计算梯度
optimizer.step()：根据梯度改参数
```

只 backward 不 step，模型不会更新。只 step 没有梯度，也不知道怎么改。

## 你可以自己改一改

把学习率改成：

```python
LEARNING_RATE = 0.001
```

再运行脚本，观察权重变化量是不是变小。

## 本节检查问题

- `loss.backward()` 和 `optimizer.step()` 分别做什么？
- 学习率太大或太小可能会有什么问题？
- 为什么训练前通常要先 `optimizer.zero_grad()`？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 7 课](07-backpropagation.md)
- 下一课：[第 9 课](09-one-batch-training-step.md)

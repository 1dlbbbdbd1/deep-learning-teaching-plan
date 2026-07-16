# PyTorch MNIST 10 小训练循环

> 核心概念：for 循环、多 batch 训练

# 第 10 课：把一次训练步骤放进小循环

这一课真正要解决的是：

```text
训练模型不是只更新一次参数，而是反复对多个 batch 做同样的训练步骤。
```

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

## 先把循环翻译成人话

```python
for step, (images, labels) in enumerate(train_loader, start=1):
```

这行的意思是：

```text
从 DataLoader 里一批一批取数据。
每次取到 images 和 labels。
step 记录这是第几步。
```

## 源码逐段讲解

### 1. 设置最多训练 5 步

```python
MAX_STEPS = 5
```

完整训练会跑很多 batch。为了新手能看清楚，这里只跑 5 个 batch。

### 2. 每个 batch 都做同样五步

```python
scores = model(images)
loss = loss_function(scores, labels)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

这就是第 9 课那套训练步骤，只是放进循环里重复执行。

### 3. 记录每一步 loss

```python
losses.append(loss.item())
print(f"第 {step} 步 loss：{loss.item():.4f}")
```

脚本把每一步 loss 存起来，并打印出来。你不是只看最后一句“通过”，而是要观察 loss 的变化。

### 4. 到第 5 步就停

```python
if step == MAX_STEPS:
    break
```

`break` 表示跳出循环。这里是为了让脚本快速结束。

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

## 输出怎么读

你会看到 5 行 loss。它们不一定每一步都下降，因为每个 batch 的图片不同。

这一课主要看：

```text
最后一步 loss 是否小于第一步 loss
```

这是一个很粗略的信号，说明模型总体在学习。

## 你真正学到了什么

训练循环不是新魔法，它只是重复第 9 课：

```text
取一个 batch -> forward -> loss -> zero_grad -> backward -> step
再取下一个 batch -> 重复
```

## 你可以自己改一改

把：

```python
MAX_STEPS = 5
```

改成：

```python
MAX_STEPS = 10
```

再运行脚本，观察打印出来的 loss 行数是不是变成 10。

## 本节检查问题

- `for step, (images, labels) in enumerate(...)` 里，`step` 是什么？
- 为什么每个 batch 都要重新 `zero_grad()`？
- 为什么 loss 会波动，而不是每一步都下降？
- `break` 在这个脚本里起什么作用？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 9 课](09-one-batch-training-step.md)
- 下一课：[第 11 课](11-one-epoch-training.md)

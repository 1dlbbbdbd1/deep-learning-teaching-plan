# PyTorch MNIST 11 完整 Epoch 训练

> 核心概念：epoch、平均 loss

# 第 11 课：训练一个完整 epoch

这一课真正要解决的是：

```text
模型看完一个 batch 不算完整训练，它要把整个训练集按 batch 看一遍。
```

## 今天只理解一个词：epoch

`epoch` 的意思是：模型把训练集完整看一遍。

MNIST 训练集有 60000 张图。如果我们设置：

```python
BATCH_SIZE = 256
```

那么模型不会一次吃下 60000 张图，而是分批吃：

```text
60000 张图 / 每批 256 张 ≈ 235 个 batch
```

所以这一课做的事是：

```text
让模型连续训练 235 个 batch，也就是看完整个训练集 1 遍
```

## 为什么 batch 数是 235

因为最后一个 batch 可能不足 256 张。

PyTorch 的 `DataLoader` 默认不会丢掉最后那个不满的 batch，所以：

```text
234 个满 batch + 1 个不满 batch = 235 个 batch
```

## 这一课怎么看模型是否在学

我们不盯着每一个 batch，因为单个 batch 的 loss 会波动。

我们看两个平均值：

```text
前 20 个 batch 平均 loss
后 20 个 batch 平均 loss
```

如果后 20 个 batch 的平均 loss 更低，就说明模型在这一遍训练中总体学到了东西。

## 源码逐段讲解

### 1. 设置训练参数

```python
BATCH_SIZE = 256
LEARNING_RATE = 0.1
EPOCHS = 1
```

这些不是固定真理，只是本课为了快速演示选择的值。

`EPOCHS = 1` 表示完整看训练集 1 遍。

### 2. 双层循环

```python
for epoch in range(EPOCHS):
    for images, labels in train_loader:
```

外层控制看几遍训练集。

内层从 DataLoader 里一批一批取数据。

### 3. 每个 batch 做训练步骤

```python
scores = model(images)
loss = loss_function(scores, labels)
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

这就是第 9 课的训练步骤，只是现在对整个训练集的每个 batch 都执行。

### 4. 记录 loss 趋势

```python
losses.append(loss.item())
```

脚本把每个 batch 的 loss 存起来。训练结束后比较前 20 个 batch 和后 20 个 batch 的平均 loss。

## 运行脚本

```powershell
python .\mnist_project\11_one_epoch_training.py
```

期待看到：

```text
epoch 数：1
训练样本数：60000
训练 batch 数：235
一个 epoch 内 loss 是否总体下降：True
完整 epoch 训练验证通过
```

## 输出怎么读

- `训练样本数：60000`：模型这一轮要看 60000 张训练图片。
- `训练 batch 数：235`：这些图片被分成 235 批。
- `前 20 个 batch 平均 loss`：训练刚开始的错误水平。
- `后 20 个 batch 平均 loss`：训练快结束时的错误水平。
- `总体下降：True`：说明模型这一轮总体在学习。

## 你真正学到了什么

`epoch` 是训练的一个完整单位：

```text
一个 epoch = 用所有训练样本训练一遍
```

以后看到训练 5 个 epoch，就是把训练集完整看 5 遍。

## 你可以自己改一改

把：

```python
BATCH_SIZE = 256
```

改成：

```python
BATCH_SIZE = 128
```

再运行脚本，观察训练 batch 数是不是变多。

## 本节检查问题

- `epoch` 和 `batch` 有什么区别？
- 为什么 60000 张图、batch size 为 256 时，batch 数是 235？
- 为什么我们比较前 20 个 batch 和后 20 个 batch 的平均 loss，而不是只比较某两个 batch？
- batch size 变小后，batch 数会变多还是变少？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 10 课](10-mini-training-loop.md)
- 下一课：[第 12 课](12-evaluate-test-set.md)

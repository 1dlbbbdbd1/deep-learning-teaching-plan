# PyTorch MNIST 11 完整 Epoch 训练

> 核心概念：epoch、平均 loss

# 第 11 课：训练一个完整 epoch

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

## 本节检查问题

- `epoch` 和 `batch` 有什么区别？
- 为什么 60000 张图、batch size 为 256 时，batch 数是 235？
- 为什么我们比较前 20 个 batch 和后 20 个 batch 的平均 loss，而不是只比较某两个 batch？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 10 课](10-mini-training-loop.md)
- 下一课：[第 12 课](12-evaluate-test-set.md)

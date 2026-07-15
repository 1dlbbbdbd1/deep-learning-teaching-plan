# PyTorch MNIST 19 Tensor 的 shape、dtype 和 device

> 核心概念：shape、dtype、device

# 第 19 课：先学会看懂 Tensor 的身份证

Tensor 是 PyTorch 里最常见的数据格式。复刻项目和 Debug 时，第一步通常不是改模型，而是确认 Tensor 的三件事：

```text
shape：长什么形状
dtype：里面是什么类型的数字
device：放在 CPU 还是 GPU
```

## shape：数据的形状

MNIST 图片常见形状是：

```text
[batch_size, 1, 28, 28]
```

它表示一批图片、1 个灰度通道、高 28、宽 28。模型报 shape 错误时，先打印输入和输出形状。

## dtype：数字类型

图片通常是 `float32`，标签通常是整数类别。分类任务用 `CrossEntropyLoss` 时，标签一般应该是类别编号，不是 one-hot。

## device：数据在哪

模型和数据必须在同一个设备上。模型在 GPU、数据在 CPU，就会报 device mismatch。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\19_inspect_tensor_metadata.py
```

看到 `Tensor 元数据验证通过`，说明你已经能检查 shape、dtype 和 device。

- 打印一个 batch 的 `images.shape`、`images.dtype`、`images.device`。
- 打印 `labels.shape`、`labels.dtype`、`labels.device`。
- 解释为什么图片和标签的 dtype 不一样。

## Debug 检查

遇到报错先问：

- 输入 shape 是否符合模型期待？
- labels 是不是类别编号？
- 模型和数据是不是在同一个 device？

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 18 课](18-decision-tree-random-forest.md)
- 下一课：[第 20 课](20-dataset-transform-normalization.md)

# PyTorch MNIST 27 池化、通道和最小 CNN

> 核心概念：pooling、channels、CNN

# 第 27 课：把卷积层连成一个小 CNN

最小 CNN 可以先长这样：

```text
Conv2d -> ReLU -> MaxPool2d -> Flatten -> Linear
```

## 池化做什么

池化会缩小特征图尺寸，让模型保留主要信息，减少计算量。

常见写法：

```python
nn.MaxPool2d(kernel_size=2)
```

## 通道会怎么变

输入 MNIST 是 1 个通道。卷积层可以输出多个通道，比如 8 个特征图。

## Flatten 前一定要算 shape

卷积和池化之后，进入 Linear 前要展平。这里最容易算错。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\27_pooling_channels_cnn.py
```

看到 `池化和最小 CNN 验证通过`，说明一个最小 CNN 能从图片输出 10 类 logits。

- 写一个最小 CNN 结构。
- 打印每层输出 shape。
- 计算 Flatten 后应该接多少输入特征。

## Debug 检查

如果 Linear 报矩阵乘法 shape 错误，通常是 Flatten 后的大小算错了。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 26 课](26-convolution-feature-map.md)
- 下一课：[第 28 课](28-train-evaluate-cnn.md)

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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| pooling | 缩小特征图，保留主要信息 | `nn.MaxPool2d(2)` |
| channel | 特征图数量 | `nn.Conv2d(1, 4, ...)` |
| Flatten | 把多维特征图摊平成一行 | `nn.Flatten()` |
| logits | 最终 10 类分数 | `logits` |

## 源码逐段讲解

### 1. 定义最小 CNN

```python
model = nn.Sequential(
    nn.Conv2d(1, 4, kernel_size=3),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    nn.Flatten(),
    nn.Linear(4 * 13 * 13, 10),
)
```

这条链路是：

```text
卷积 -> 激活 -> 池化 -> 展平 -> 分类
```

### 2. 为什么 Linear 是 `4 * 13 * 13`

输入图片是 28x28。

卷积核 3x3、不补边：

```text
28 - 3 + 1 = 26
```

池化 `kernel_size=2` 会把 26x26 缩成 13x13。

卷积输出 4 个通道，所以展平后是：

```text
4 * 13 * 13
```

### 3. 造两张随机图片

```python
images = torch.randn(2, 1, 28, 28)
```

shape 是 `[2, 1, 28, 28]`，表示 2 张 MNIST 格式图片。

### 4. 得到 logits

```python
logits = model(images)
```

输出应该是 `[2, 10]`：2 张图，每张图 10 个类别分数。

## 输出怎么读

- `输入图片 shape：[2, 1, 28, 28]`：2 张灰度图。
- `模型结构`：从卷积到分类的顺序。
- `输出 logits shape：[2, 10]`：最终能接分类 loss。

## 你真正学到了什么

CNN 最容易卡在 `Flatten -> Linear` 这里。

以后看到这种错误：

```text
mat1 and mat2 shapes cannot be multiplied
```

第一反应应该是：Flatten 后的大小和 Linear 的输入大小不一致。

## 你可以自己改一改

把：

```python
nn.Conv2d(1, 4, kernel_size=3)
nn.Linear(4 * 13 * 13, 10)
```

临时改成：

```python
nn.Conv2d(1, 8, kernel_size=3)
nn.Linear(8 * 13 * 13, 10)
```

再运行脚本。输出仍然应该是 `[2, 10]`，只是通道数变多了。

## Debug 检查

如果 Linear 报矩阵乘法 shape 错误，通常是 Flatten 后的大小算错了。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 26 课](26-convolution-feature-map.md)
- 下一课：[第 28 课](28-train-evaluate-cnn.md)

# PyTorch MNIST 26 卷积、卷积核和特征图

> 核心概念：Conv2d、kernel、feature map

# 第 26 课：CNN 为什么适合图片

MLP 会把图片展平成一行，这会丢掉空间结构。CNN 会保留图片的高和宽，用卷积核在图片上滑动。

```text
图片 -> 卷积核扫描 -> 特征图
```

## 卷积核是什么

卷积核可以理解成一个小窗口。它在图片上移动，检测某种局部模式，比如边缘或笔画。

## 特征图是什么

卷积层输出的结果叫 feature map。它表示某个卷积核在不同位置看到了什么。

## Conv2d 的常见参数

```python
nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3)
```

- `in_channels=1`：输入是灰度图。
- `out_channels=8`：学 8 组卷积核。
- `kernel_size=3`：每次看 3x3 的局部区域。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\26_convolution_feature_map.py
```

看到 `卷积和特征图验证通过`，说明你已经观察过 Conv2d 如何产生 feature map。

- 写出输入图片 shape。
- 写出卷积层输出 shape。
- 解释 `out_channels` 为什么会变成新的通道数。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| Conv2d | 处理图片的卷积层 | `nn.Conv2d(...)` |
| kernel | 小窗口/卷积核 | `kernel_size=3` |
| feature map | 卷积后得到的新图 | `feature_maps` |
| channel | 通道数 | `in_channels`、`out_channels` |

## 源码逐段讲解

### 1. 造一张 6x6 小图片

```python
image = torch.zeros(1, 1, 6, 6)
image[:, :, 2:4, 2:4] = 1.0
```

shape `[1, 1, 6, 6]` 表示：

```text
1 张图片、1 个通道、高 6、宽 6
```

第二行把图片中间一小块变亮。

### 2. 创建卷积层

```python
conv = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=3)
```

这行表示：

- 输入是 1 通道图片。
- 输出 2 张特征图。
- 每个卷积核看 3x3 的小区域。

### 3. 让卷积核扫描图片

```python
feature_maps = conv(image)
```

输入是 `[1, 1, 6, 6]`，输出是 `[1, 2, 4, 4]`。

为什么高宽从 6 变成 4？

因为 3x3 的窗口在 6x6 图片上不补边滑动，只能放出 4 个位置：

```text
6 - 3 + 1 = 4
```

### 4. 看卷积核参数 shape

```python
conv.weight.shape
```

它通常是：

```text
[out_channels, in_channels, kernel_height, kernel_width]
```

本课就是 `[2, 1, 3, 3]`。

## 输出怎么读

- `输入图片 shape：[1, 1, 6, 6]`：1 张 6x6 灰度图。
- `卷积核 shape：[2, 1, 3, 3]`：2 个卷积核，每个看 1 通道的 3x3 区域。
- `特征图 shape：[1, 2, 4, 4]`：输出 2 个 4x4 特征图。

## 你真正学到了什么

CNN 不是先把图片摊平，而是保留空间结构，用小窗口扫描局部区域。

读 `Conv2d` 时先看三件事：

```text
输入通道 in_channels
输出通道 out_channels
卷积核大小 kernel_size
```

## 你可以自己改一改

把：

```python
out_channels=2
```

临时改成：

```python
out_channels=4
```

再运行脚本。你会看到特征图 shape 的第二维从 2 变成 4。

注意：脚本里的检查也要同步改，否则会故意报错。

## Debug 检查

CNN 常见错误是通道数不匹配。看到 Conv2d 报错，先查 `[batch, channel, height, width]`。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 25 课](25-hyperparameters-overfitting.md)
- 下一课：[第 27 课](27-pooling-channels-cnn.md)

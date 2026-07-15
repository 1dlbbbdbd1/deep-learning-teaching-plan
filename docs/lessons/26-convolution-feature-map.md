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

## Debug 检查

CNN 常见错误是通道数不匹配。看到 Conv2d 报错，先查 `[batch, channel, height, width]`。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 25 课](25-hyperparameters-overfitting.md)
- 下一课：[第 27 课](27-pooling-channels-cnn.md)

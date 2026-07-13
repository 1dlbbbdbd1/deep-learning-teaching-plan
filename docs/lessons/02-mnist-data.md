# PyTorch MNIST 02 认识 MNIST 数据

> 核心概念：Dataset、Tensor、像素范围

# 第 2 课：认识 MNIST 数据

## 今天只理解两个词

1. **样本**：一条训练数据。MNIST 里一条样本就是“一张手写数字图片 + 它的数字标签”。
2. **张量**：PyTorch 处理数据的主要格式。你可以先把它理解成“更适合计算的多维数组”。

## MNIST 一张图是什么样

MNIST 的图片是灰度图，所以一张图会变成这个形状：

```text
torch.Size([1, 28, 28])
```

三个数字分别表示：

- `1`：一个颜色通道，因为灰度图只有黑白深浅。
- `28`：图片高度 28 像素。
- `28`：图片宽度 28 像素。

标签是 `0` 到 `9` 中的一个整数，表示这张图上写的是哪个数字。

## 运行脚本

```powershell
python .\mnist_project\02_inspect_mnist_data.py
```

第一次运行会下载 MNIST 到项目里的 `data/` 目录。这个目录已经写进 `.gitignore`，以后不会被 Git 收进去。

期待看到：

```text
训练集样本数：60000
第一张图片的标签：5
图片张量形状：torch.Size([1, 28, 28])
MNIST 数据验证通过
```

## 本节检查问题

- `torch.Size([1, 28, 28])` 里的三个数字分别表示什么？
- 为什么标签只可能是 `0` 到 `9`？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 1 课](01-pytorch-installation.md)
- 下一课：[第 3 课](03-mnist-visualization.md)

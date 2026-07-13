# PyTorch MNIST 03 保存并查看手写数字图片

> 核心概念：PIL、灰度图、outputs 目录

# 第 3 课：把 MNIST 图片保存出来看一眼

## 今天只理解两个词

1. **PIL 图片**：Python 里常见的一种图片对象，可以直接保存成 `.png`。
2. **可视化**：把数据变成你能看的东西。对新手来说，这比盯着一堆数字更踏实。

上一课我们看到第一张图片的张量形状是：

```text
torch.Size([1, 28, 28])
```

这一课先不训练模型，只把第一张图片保存出来。

## 运行脚本

```powershell
python .\mnist_project\03_save_mnist_image.py
```

期待看到：

```text
第一张图片的标签：5
图片模式：L
图片尺寸：(28, 28)
保存图片：outputs\mnist_sample_0_label_5.png
MNIST 图片保存验证通过
```

然后打开：

```text
outputs\mnist_sample_0_label_5.png
```

你应该能看到一张很小的手写数字 `5`。

## 本节检查问题

- 为什么脚本保存出来的文件名里带着 `label_5`？
- `图片尺寸：(28, 28)` 和上一课的 `torch.Size([1, 28, 28])` 有什么关系？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 2 课](02-mnist-data.md)
- 下一课：[第 4 课](04-dataloader-batches.md)

# PyTorch MNIST 04 DataLoader 和 Batch

> 核心概念：DataLoader、batch、shape

# 第 4 课：用 DataLoader 批量取样本

## 今天只理解两个词

1. **DataLoader**：PyTorch 用来“按批次取数据”的工具。
2. **batch**：一小批样本。训练神经网络时通常不是一张一张喂，而是一批一批喂。

上一课一张 MNIST 图片的形状是：

```text
torch.Size([1, 28, 28])
```

这一课一次取 32 张图片，所以图片 batch 的形状会变成：

```text
torch.Size([32, 1, 28, 28])
```

这四个数字分别是：

- `32`：这一批里有 32 张图片。
- `1`：每张图片 1 个灰度通道。
- `28`：每张图片高 28 像素。
- `28`：每张图片宽 28 像素。

标签 batch 的形状是：

```text
torch.Size([32])
```

意思是这 32 张图片对应 32 个数字标签。

## 运行脚本

```powershell
python .\mnist_project\04_inspect_dataloader_batch.py
```

期待看到：

```text
batch size：32
图片 batch 形状：torch.Size([32, 1, 28, 28])
标签 batch 形状：torch.Size([32])
DataLoader batch 验证通过
```

## 本节检查问题

- `torch.Size([32, 1, 28, 28])` 里多出来的 `32` 表示什么？
- 为什么标签 batch 是 `torch.Size([32])`，而不是 `torch.Size([32, 1, 28, 28])`？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 3 课](03-mnist-visualization.md)
- 下一课：[第 5 课](05-minimal-model-forward.md)

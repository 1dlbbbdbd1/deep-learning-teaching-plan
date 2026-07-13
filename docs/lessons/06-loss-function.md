# PyTorch MNIST 06 交叉熵损失

> 核心概念：CrossEntropyLoss、loss 标量

# 第 6 课：计算一次分类损失

## 今天只理解两个词

1. **loss**：一个数字，用来表示模型当前猜得有多差。
2. **CrossEntropyLoss**：分类任务常用的损失函数。手写数字识别是 10 分类，所以先用它。

上一课模型输出：

```text
torch.Size([32, 10])
```

意思是 32 张图，每张图有 10 个分数。

真实标签是：

```text
torch.Size([32])
```

意思是 32 张图各有 1 个正确答案。

损失函数做的事可以先粗略理解为：

```text
模型的 10 个分数 + 正确答案 -> 一个 loss 数字
```

## 运行脚本

```powershell
python .\mnist_project\06_compute_loss.py
```

期待看到：

```text
模型输出形状：torch.Size([32, 10])
真实标签形状：torch.Size([32])
loss 形状：torch.Size([])
loss 数值：...
损失函数验证通过
```

## 为什么 loss 形状是空的

`torch.Size([])` 表示这是一个标量，也就是单独一个数字。它不是一张图，也不是一批标签，而是对这一批样本整体算出来的“错得有多厉害”。

## 本节检查问题

- 为什么模型输出是 `[32, 10]`，真实标签却是 `[32]`？
- loss 数值越小，一般表示模型越好还是越差？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 5 课](05-minimal-model-forward.md)
- 下一课：[第 7 课](07-backpropagation.md)

# PyTorch MNIST 05 最小模型前向传播

> 核心概念：Flatten、Linear、forward

# 第 5 课：写一个最小模型前向传播

## 今天只理解三个词

1. **Flatten**：把 `1 x 28 x 28` 的图片压平成一行 `784` 个数字。
2. **Linear**：最简单的一层神经网络，把一组输入数字变成一组输出数字。
3. **前向传播**：数据从输入经过模型，得到输出分数的过程。

上一课我们拿到一批图片：

```text
torch.Size([32, 1, 28, 28])
```

这节课让模型输出：

```text
torch.Size([32, 10])
```

含义是：这一批有 32 张图，每张图输出 10 个分数，分别对应数字 `0` 到 `9`。

## 模型结构

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)
```

先不用背 `nn.Sequential`。你可以把它理解成“按顺序执行两个步骤”：

```text
图片 batch -> 压平 -> 线性层 -> 10 个分数
```

## 运行脚本

```powershell
python .\mnist_project\05_minimal_model_forward.py
```

期待看到：

```text
输入图片 batch 形状：torch.Size([32, 1, 28, 28])
展平后 batch 形状：torch.Size([32, 784])
模型输出形状：torch.Size([32, 10])
最小模型前向传播验证通过
```

## 一个重要提醒

现在模型还没有训练，所以 10 个分数只是随机初始化权重算出来的结果。它现在“会输出”，但还“不懂数字”。

下一课才会引入“损失函数”，用来衡量模型猜得有多离谱。

## 本节检查问题

- 为什么 `1 x 28 x 28` 展平后是 `784`？
- 为什么最终输出是 `10` 个分数？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 4 课](04-dataloader-batches.md)
- 下一课：[第 6 课](06-loss-function.md)

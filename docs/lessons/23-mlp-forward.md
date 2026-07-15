# PyTorch MNIST 23 MLP 前向传播

> 核心概念：MLP、hidden layer、logits

# 第 23 课：把线性模型升级成 MLP

MLP 可以先理解成“带隐藏层的线性分类模型”。

```text
图片 -> 展平 -> Linear -> ReLU -> Linear -> logits
```

## hidden layer 是什么

隐藏层不是直接输出答案，而是学习中间表示。比如它可能学到笔画粗细、局部黑白分布等粗糙特征。

## 输出仍然是 logits

MNIST 有 10 类，所以最终输出仍然是 10 个分数：

```text
[batch_size, 10]
```

## MLP 和前面线性模型的区别

前面的模型：

```text
784 -> 10
```

MLP：

```text
784 -> hidden -> 10
```

中间多了一层表达能力。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\23_mlp_forward.py
```

看到 `MLP 前向传播验证通过`，说明 MLP 能把一批图片变成 10 类 logits。

- 写出 MLP 每一层输入输出 shape。
- 确认最后输出是 `[batch_size, 10]`。
- 用 `CrossEntropyLoss` 计算 loss。

## Debug 检查

如果最后一层输出不是 10，MNIST 分类就对不上。先查输出 shape，再查 loss。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 22 课](22-activation-functions.md)
- 下一课：[第 24 课](24-train-mnist-mlp.md)

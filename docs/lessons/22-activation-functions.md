# PyTorch MNIST 22 激活函数为什么有用

> 核心概念：ReLU、非线性、隐藏层

# 第 22 课：只叠线性层还不够

如果模型只有线性层，很多层叠在一起，本质上仍然像一个更大的线性变换。激活函数给模型加入非线性能力。

最常见的激活函数之一是：

```python
nn.ReLU()
```

## ReLU 做什么

ReLU 的规则很简单：

```text
小于 0 的数变成 0
大于 0 的数保持不变
```

## 为什么要非线性

现实数据通常不是一条直线能分开的。隐藏层加激活函数，模型才能表达更复杂的边界。

## 在 MLP 里怎么用

常见结构：

```text
Linear -> ReLU -> Linear -> logits
```

第一个 Linear 提取中间特征，ReLU 增加非线性，最后 Linear 输出类别分数。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\22_activation_functions.py
```

看到 `激活函数验证通过`，说明你已经观察过 ReLU 如何处理负数和正数。

- 找到模型里的 `ReLU`。
- 说明它前后分别是什么层。
- 打印 ReLU 前后的数值范围。

## Debug 检查

如果 loss 不下降，检查学习率、输入范围和激活函数位置。不要一上来就把模型改得很复杂。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 21 课](21-custom-nn-module.md)
- 下一课：[第 23 课](23-mlp-forward.md)

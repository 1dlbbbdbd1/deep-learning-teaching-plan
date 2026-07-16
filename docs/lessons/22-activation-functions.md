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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| activation | 激活函数，给模型加“转弯能力” | `nn.ReLU()` |
| ReLU | 负数变 0，正数不动 | `relu(values)` |
| non-linear | 不是一条直线能表达的关系 | `Linear -> ReLU -> Linear` |
| hidden layer | 中间层 | 第 21、23 课的 hidden 层 |

## 源码逐段讲解

### 1. 准备一排数字

```python
values = torch.tensor([[-2.0, -0.5, 0.0, 1.0, 3.0]])
```

这里故意放了负数、0 和正数，方便观察 ReLU 的规则。

### 2. 创建 ReLU

```python
relu = nn.ReLU()
```

`ReLU` 的规则很简单：

```text
小于 0 -> 变成 0
大于等于 0 -> 保持原样
```

### 3. 执行激活函数

```python
activated = relu(values)
```

这行会得到新 Tensor。原来的负数会被压成 0。

### 4. 检查 ReLU 后没有负数

```python
if activated.min().item() < 0:
    raise RuntimeError("ReLU 后不应该有负数。")
```

`activated.min()` 取最小值。如果 ReLU 正常，最小值应该至少是 0。

## 输出怎么读

- `ReLU 前`：包含负数和正数。
- `ReLU 后`：负数变成 0，正数保留。
- `ReLU 后最小值：0.0`：说明输出里已经没有负数。

## 你真正学到了什么

激活函数让神经网络不只是“线性层堆线性层”。

先不用深究数学证明，只要记住这条直觉：

```text
Linear 负责算一组新数字
ReLU 负责加入非线性变化
二者组合后，模型表达能力更强
```

## 你可以自己改一改

把输入改成：

```python
values = torch.tensor([[5.0, -3.0, 2.0]])
```

再运行脚本。你会看到 `-3.0` 被变成 `0.0`，其他正数保持不变。

## Debug 检查

如果 loss 不下降，检查学习率、输入范围和激活函数位置。不要一上来就把模型改得很复杂。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 21 课](21-custom-nn-module.md)
- 下一课：[第 23 课](23-mlp-forward.md)

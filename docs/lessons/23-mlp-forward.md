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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| MLP | 多层感知机，可以先理解成带隐藏层的分类模型 | `nn.Sequential(...)` |
| hidden size | 隐藏层宽度 | `nn.Linear(28 * 28, 32)` |
| logits | 每个类别的原始分数 | `logits = model(images)` |
| `argmax` | 找最高分对应的类别编号 | `logits.argmax(dim=1)` |

## 源码逐段讲解

### 1. 设置 batch size

```python
BATCH_SIZE = 5
```

这一课不用真实 MNIST，而是造 5 张随机图片，只验证 MLP 的前向传播 shape。

### 2. 定义 MLP

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)
```

这条流水线可以读成：

```text
[5, 1, 28, 28]
-> Flatten 后 [5, 784]
-> Linear 后 [5, 32]
-> ReLU 后 [5, 32]
-> Linear 后 [5, 10]
```

### 3. 造一批随机图片

```python
images = torch.randn(BATCH_SIZE, 1, 28, 28)
```

`randn` 会生成随机小数。这里不是为了训练，只是为了让模型有输入。

### 4. 执行前向传播

```python
logits = model(images)
```

模型输出 logits。MNIST 有 10 类，所以最后一维必须是 10。

### 5. 取预测类别

```python
logits.argmax(dim=1)
```

`dim=1` 表示在“类别分数”这一维找最大值。

## 输出怎么读

- `输入图片 shape：[5, 1, 28, 28]`：5 张 MNIST 格式图片。
- `MLP 输出 logits shape：[5, 10]`：每张图片 10 个类别分数。
- `第一张图片的预测类别`：当前随机模型最高分对应的类别，不代表真的会识别。

## 你真正学到了什么

MLP 比线性模型多了隐藏层和激活函数，但最后仍然要输出 `[batch_size, 10]`。

读模型时最稳的办法是一路追 shape：

```text
输入 shape -> 每层输出 shape -> 最终 logits shape
```

## 你可以自己改一改

把：

```python
nn.Linear(28 * 28, 32)
nn.Linear(32, 10)
```

改成：

```python
nn.Linear(28 * 28, 64)
nn.Linear(64, 10)
```

再运行脚本。输出仍然应该是 `[5, 10]`，中间隐藏层只是变宽了。

## Debug 检查

如果最后一层输出不是 10，MNIST 分类就对不上。先查输出 shape，再查 loss。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 22 课](22-activation-functions.md)
- 下一课：[第 24 课](24-train-mnist-mlp.md)

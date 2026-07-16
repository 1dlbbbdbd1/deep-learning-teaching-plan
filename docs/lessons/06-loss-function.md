# PyTorch MNIST 06 交叉熵损失

> 核心概念：CrossEntropyLoss、loss 标量

# 第 6 课：计算一次分类损失

这一课真正要解决的是：

```text
模型输出 10 个分数以后，程序怎么知道它猜得好不好？
```

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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| loss | 错误程度的数字 | `loss` |
| loss function | 计算错误程度的规则 | `loss_function` |
| CrossEntropyLoss | 多分类常用的 loss | `nn.CrossEntropyLoss()` |
| scores | 模型输出的 10 个分数 | `scores = model(images)` |
| labels | 正确答案 | `labels` |

## 源码逐段讲解

### 1. 先得到模型分数

```python
scores = model(images)
```

`scores` 的形状是 `[32, 10]`。

32 表示 32 张图片，10 表示每张图片对应 10 个数字类别的分数。

### 2. 准备损失函数

```python
loss_function = nn.CrossEntropyLoss()
```

这是 PyTorch 提供的分类损失函数。

它会比较：

```text
模型输出的 10 个分数
真实标签
```

然后算出一个 loss。

### 3. 计算 loss

```python
loss = loss_function(scores, labels)
```

这里传入两个东西：

- `scores`：模型猜出来的分数。
- `labels`：正确答案。

输出 `loss` 是一个数字，表示这批样本整体错得多不多。

## 一个容易误会的点

`CrossEntropyLoss` 里传入的是原始分数，不需要你先手动转成概率。

也就是说，先不要自己加 softmax。PyTorch 会在内部处理需要的计算。

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

## 输出怎么读

- `模型输出形状：[32, 10]`：32 张图，每张图 10 个分数。
- `真实标签形状：[32]`：32 张图，每张图 1 个正确答案。
- `loss 形状：[]`：loss 是一个单独数字。
- `loss 数值`：当前模型在这一批样本上的错误程度。

因为模型还没训练，所以 loss 通常不会很低。

## 你真正学到了什么

模型光能输出分数还不够，训练必须有一个“评分规则”。

`CrossEntropyLoss` 在这一课里扮演的角色就是：

```text
看模型给 10 个类别打的分，再看正确答案，最后给出一个错误程度数字
```

这个错误程度数字后面会被反向传播使用。也就是说，loss 是训练链条里的中间枢纽：

```text
模型输出 -> loss -> 梯度 -> 参数更新
```

## 你可以自己改一改

把脚本里的：

```python
labels
```

临时换成：

```python
labels[:10]
```

你会看到程序报错，因为 scores 有 32 条，但 labels 只有 10 条。这个实验能帮你理解：分数和标签必须一一对应。

## 本节检查问题

- 为什么模型输出是 `[32, 10]`，真实标签却是 `[32]`？
- loss 数值越小，一般表示模型越好还是越差？
- `CrossEntropyLoss` 需要的是概率，还是模型原始分数？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 5 课](05-minimal-model-forward.md)
- 下一课：[第 7 课](07-backpropagation.md)

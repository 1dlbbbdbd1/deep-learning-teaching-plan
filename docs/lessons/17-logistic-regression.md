# PyTorch MNIST 17 逻辑回归

> 核心概念：分类、logits、概率、交叉熵

# 第 17 课：逻辑回归为什么叫“回归”，却用来分类

逻辑回归这个名字很容易误导人。它通常不是用来预测连续数字，而是用来做分类。

比如：

```text
邮件 -> 垃圾邮件或正常邮件
图片 -> 猫或狗
手写数字 -> 0 到 9
```

你可以先把它理解成：在线性模型后面接一个“变成分类判断”的步骤。

## 二分类的直觉

二分类只有两个答案，比如：

```text
是不是垃圾邮件
是不是生病
是不是会点击
```

模型先输出一个分数。分数越大，越偏向“是”；分数越小，越偏向“否”。

这个分数可以再转成 0 到 1 之间的概率。

## 多分类的直觉

MNIST 是多分类，因为答案有 10 个：

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

之前的模型输出 10 个分数：

```text
[数字0的分数, 数字1的分数, ..., 数字9的分数]
```

这些分数叫 logits。它们还不是概率，但可以用来计算交叉熵损失，也可以用 `argmax` 找最高分对应的类别。

## 为什么用交叉熵

分类问题最关心的是：正确类别的分数够不够高，错误类别的分数有没有被压下去。

交叉熵就是一种衡量方式。它会鼓励模型把正确类别的分数提高。

在 PyTorch 里，常见写法是：

```python
loss_fn = torch.nn.CrossEntropyLoss()
loss = loss_fn(logits, labels)
```

注意：这里传入的是 logits，不需要自己先做 softmax。

## MNIST 线性模型其实已经很接近逻辑回归

前面 00-14 的 MNIST 模型结构很简单：

```text
图片 -> 展平 -> 线性层 -> 10 个 logits -> 交叉熵 -> 更新参数
```

这就是一个最小的线性分类模型。理解逻辑回归后，你会发现自己已经跑通过一个分类模型闭环了。

## Debug 时先查什么

分类任务里常见错误有三类：

- logits 的形状不对，应该常见为 `[batch_size, class_count]`。
- labels 的形状不对，通常应该是 `[batch_size]`。
- labels 的类型不对，交叉熵通常需要类别编号，而不是 one-hot 向量。

如果 loss 报错，先打印：

```python
print(logits.shape)
print(labels.shape)
print(labels.dtype)
```

## 运行脚本

```powershell
python .\mnist_project\17_train_logistic_regression.py
```

期待看到：

```text
类别数：2
初始 loss：...
最终 loss：...
训练集准确率：1.00
逻辑回归训练验证通过
```

这个脚本用 6 条人工造的小数据训练一个二分类模型。重点不是数据多大，而是看清楚 logits、标签、交叉熵和准确率如何连起来。

## 源码逐段讲解

### 1. 准备二分类数据

```python
features = torch.tensor(
    [
        [-2.0, -1.0],
        ...
        [2.0, 2.0],
    ]
)
labels = torch.tensor([0, 0, 0, 1, 1, 1])
```

这里每条样本有 2 个特征，所以 `features.shape` 是 `[6, 2]`。

标签只有两类：`0` 和 `1`。这就是二分类。

### 2. 创建分类模型

```python
model = nn.Linear(2, 2)
```

第一个 `2`：输入有 2 个特征。

第二个 `2`：输出 2 个类别分数。

所以模型输出的 logits 形状会是：

```text
[6, 2]
```

意思是 6 条样本，每条样本有 2 个类别分数。

### 3. 用交叉熵计算分类错误

```python
loss_function = nn.CrossEntropyLoss()
```

`CrossEntropyLoss` 会拿两样东西：

```text
logits: [样本数, 类别数]
labels: [样本数]
```

然后算出一个 loss。

### 4. 训练循环仍然是老五步

```python
logits = model(features)
loss = loss_function(logits, labels)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

你会发现，回归和分类的训练骨架很像。真正变的是：

- 模型输出含义不同。
- loss 函数不同。
- 评估指标不同。

### 5. 用 argmax 得到预测类别

```python
predictions = final_logits.argmax(dim=1)
```

`argmax(dim=1)` 的意思是：对每一行 logits，找到分数最高的类别编号。

如果一条样本的 logits 是：

```text
[-1.2, 2.5]
```

最高分在第 1 类，所以预测结果是 `1`。

## 输出怎么读

- `类别数：2`：这是二分类，不是 MNIST 那种 10 分类。
- `初始 loss`：训练前分类错得多不多。
- `最终 loss`：训练后应该下降。
- `训练集准确率：1.00`：6 条小样本都分对了。
- `预测结果：[0, 0, 0, 1, 1, 1]`：和标签一致。

这份数据太小，所以准确率 1.00 不代表真实项目一定泛化好。它只说明逻辑回归训练流程跑通了。

## 你真正学到了什么

逻辑回归虽然名字里有“回归”，但在这里它是在做分类。

它的核心链条是：

```text
特征 -> 线性层 -> logits -> CrossEntropyLoss -> 参数更新
```

这条链条和 MNIST 线性分类模型非常接近，所以学它是为了帮你看懂前面已经跑过的分类模型。

## 你可以自己改一改

把：

```python
LEARNING_RATE = 0.2
```

临时改成：

```python
LEARNING_RATE = 0.001
```

再运行脚本。你可能会看到 loss 降得不够，准确率不如原来。

这个实验想让你理解：学习率太小，模型可能学得很慢。

## 本节小练习

不写代码，先用自己的话回答：

- 逻辑回归主要解决回归问题，还是分类问题？
- logits 和概率有什么区别？
- MNIST 为什么是多分类？
- 为什么 `CrossEntropyLoss` 里通常直接传 logits？

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 16 课](16-linear-regression.md)
- 第 06 课：[交叉熵损失](06-loss-function.md)
- 第 14 课：[加载模型并预测单张图片](14-load-model-and-predict.md)

# PyTorch MNIST 05 最小模型前向传播

> 核心概念：Flatten、Linear、forward

# 第 5 课：写一个最小模型前向传播

这一课真正要解决的是：

```text
一批图片进入模型后，模型为什么会输出 10 个数字分数？
```

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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| `nn` | PyTorch 里搭模型的工具箱 | `from torch import nn` |
| `Flatten` | 把图片摊平成一行数字 | `nn.Flatten()` |
| `Linear` | 一层最简单的可学习计算 | `nn.Linear(28 * 28, 10)` |
| logits / 分数 | 模型对每个类别给出的原始分数 | `scores` |
| forward | 数据从输入流到输出 | `scores = model(images)` |

## 源码逐段讲解

### 1. 取出一个 batch

脚本前半部分和第 4 课一样：加载 MNIST，用 DataLoader 取出 32 张图片。

```python
images, labels = next(iter(train_loader))
```

此时：

```text
images.shape = [32, 1, 28, 28]
labels.shape = [32]
```

### 2. 定义模型

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)
```

`nn.Sequential` 表示按顺序执行里面的层。

第一层 `Flatten()` 把每张图片从 `[1, 28, 28]` 变成 `[784]`。

第二层 `Linear(784, 10)` 把 784 个输入数字变成 10 个输出分数。

### 3. 前向传播

```python
scores = model(images)
```

这行就是把一批图片送进模型。

输出 `scores` 的形状是：

```text
[32, 10]
```

意思是：32 张图片，每张图片都有 10 个分数。

### 4. 为什么用 `torch.no_grad()`

```python
with torch.no_grad():
```

这一课只是观察模型输出，不训练参数，所以不用计算梯度。`no_grad()` 可以先理解成“只看结果，不准备学习”。

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

## 输出怎么读

- `输入图片 batch 形状：[32, 1, 28, 28]`：模型拿到 32 张图片。
- `展平后 batch 形状：[32, 784]`：每张图片被摊平成 784 个数字。
- `模型输出形状：[32, 10]`：每张图片得到 10 个类别分数。
- `第一张图片的 10 个分数`：这些是未训练模型随便算出来的原始分数。

不要把最高分当成“模型已经会了”。这时模型还没训练，只是能算出输出。

## 你真正学到了什么

这一课不是让你记住 `nn.Sequential` 这个名字，而是让你看懂一条最小模型流水线：

```text
图片 batch -> Flatten 展平 -> Linear 计算 -> 每张图 10 个分数
```

以后看到别人的模型代码时，你可以先问两个问题：

1. 输入 shape 是什么？
2. 输出 shape 是什么？

只要这两个问题能对上，模型结构就不再是一团黑盒。

## 你可以自己改一改

把：

```python
nn.Linear(28 * 28, 10)
```

临时改成：

```python
nn.Linear(28 * 28, 5)
```

再运行脚本。你会看到输出形状变成 `[32, 5]`，但这对 MNIST 是错的，因为 MNIST 有 10 个类别。

## 本节检查问题

- 为什么 `1 x 28 x 28` 展平后是 `784`？
- 为什么最终输出是 `10` 个分数？
- 为什么这一课的模型“能输出”，但还“不懂数字”？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 4 课](04-dataloader-batches.md)
- 下一课：[第 6 课](06-loss-function.md)

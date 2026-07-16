# PyTorch MNIST 21 自己写一个 nn.Module

> 核心概念：nn.Module、__init__、forward

# 第 21 课：模型是一个会 forward 的对象

前面用过 `nn.Sequential`。后面复刻项目时，更常见的是自己写一个类：

```python
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        ...

    def forward(self, x):
        ...
        return x
```

## `__init__` 放什么

`__init__` 里放模型的层，比如 `Linear`、`Conv2d`、`ReLU`。

## `forward` 放什么

`forward` 描述数据怎么流过这些层。你可以把它理解成模型的计算路线图。

## 为什么复刻项目要先看 forward

因为 forward 能告诉你：

- 输入 shape 期待是什么。
- 中间经过哪些层。
- 输出 shape 应该是什么。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\21_custom_nn_module.py
```

看到 `自定义 nn.Module 验证通过`，说明你已经能读懂 `__init__` 和 `forward` 的最小结构。

- 找一个模型类，圈出 `__init__` 和 `forward`。
- 用一句话解释每一层的作用。
- 在 forward 里临时打印关键 shape。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| `nn.Module` | PyTorch 里所有模型类的基类 | `class TinyClassifier(nn.Module)` |
| `__init__` | 准备模型零件的地方 | `self.flatten`、`self.hidden` |
| `forward` | 规定数据怎么流过模型 | `def forward(self, images)` |
| hidden layer | 中间层，不直接给最终答案 | `self.hidden` |
| logits | 最后一层输出的类别分数 | `return self.output(x)` |

## 源码逐段讲解

### 1. 定义模型类

```python
class TinyClassifier(nn.Module):
```

这表示 `TinyClassifier` 是一个 PyTorch 模型。继承 `nn.Module` 后，PyTorch 才能管理它的参数。

### 2. 在 `__init__` 里准备层

```python
self.flatten = nn.Flatten()
self.hidden = nn.Linear(28 * 28, 16)
self.activation = nn.ReLU()
self.output = nn.Linear(16, 10)
```

这些是模型的零件：

```text
Flatten：把图片摊平
hidden：把 784 个像素变成 16 个中间特征
ReLU：加入非线性
output：把 16 个中间特征变成 10 个类别分数
```

### 3. 在 `forward` 里安排数据路线

```python
x = self.flatten(images)
x = self.hidden(x)
x = self.activation(x)
return self.output(x)
```

这段就是模型的计算路线图。

你可以在每一行后面临时加：

```python
print(x.shape)
```

用来定位 shape 从哪一步开始不对。

### 4. 创建模型并喂入假图片

```python
model = TinyClassifier()
images = torch.zeros(3, 1, 28, 28)
logits = model(images)
```

这里的 `model(images)` 会自动调用 `forward(images)`。

## 输出怎么读

- `print(model)`：显示模型有哪些层。
- `输入 shape：[3, 1, 28, 28]`：3 张 MNIST 格式图片。
- `输出 logits shape：[3, 10]`：每张图片有 10 个类别分数。

## 你真正学到了什么

`nn.Module` 不是玄学。你只要先抓住两个地方：

```text
__init__：模型有哪些层
forward：数据按什么顺序经过这些层
```

复刻项目时，先读 `forward`，往往比先读训练脚本更快找到模型输入输出逻辑。

## 你可以自己改一改

把：

```python
self.hidden = nn.Linear(28 * 28, 16)
self.output = nn.Linear(16, 10)
```

临时改成：

```python
self.hidden = nn.Linear(28 * 28, 32)
self.output = nn.Linear(32, 10)
```

再运行脚本。你会发现输出仍然是 `[3, 10]`，只是中间隐藏层变宽了。

## Debug 检查

如果模型运行失败，先不要乱改层数。先确认 forward 里哪一步 shape 开始不对。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 20 课](20-dataset-transform-normalization.md)
- 下一课：[第 22 课](22-activation-functions.md)

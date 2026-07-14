# PyTorch MNIST 01.5 PyTorch 常用功能速览

> 核心概念：torch、Tensor、Dataset、DataLoader、nn、loss、optimizer

# 第 1.5 课：先认识 PyTorch 的常用部件

你现在不需要掌握 PyTorch 的全部功能。先把以后会反复见到的几个名字混个脸熟就够了。

这一课的目标不是写代码，而是回答一个问题：

```text
以后看到 PyTorch 代码时，我大概知道每一块在干什么。
```

## 为什么第 2 课之前要先看这个

第 1 课只是在确认 PyTorch 安装好了。它证明工具能用，但还没有告诉你工具箱里有什么。

如果第 2 课直接看到 `datasets.MNIST`、`transforms.ToTensor()`、`image.shape`，很容易懵。不是你笨，是地图少了一张。

## PyTorch 最常见的 6 类东西

先记住这张表：

| 名字 | 它大概负责什么 | 以后在哪会见到 |
| --- | --- | --- |
| `torch` | PyTorch 的总入口 | 创建张量、保存模型、检查 GPU |
| `Tensor` | 数据的主要格式 | 图片、标签、模型输入、模型输出 |
| `Dataset` | 管一堆样本 | MNIST 训练集和测试集 |
| `DataLoader` | 分批取数据 | 每次拿一批图片训练 |
| `nn` | 搭模型的积木 | 线性层、卷积层、激活函数 |
| `optimizer` | 更新模型参数 | SGD、Adam |

你现在不用背 API，只要知道它们大概属于哪一层。

## 用做饭来理解

可以先这样想：

```text
Dataset：冰箱，里面放着很多食材
DataLoader：每次拿出一小篮食材
Tensor：食材被切成机器能处理的格式
nn.Module：锅和菜谱，也就是模型
loss：尝一口，判断差多少
optimizer：根据味道调整下一次怎么做
```

这个比喻不严谨，但对入门够用。后面每节课会逐个把它们换回正式概念。

## 以后代码会长成什么样

后面很多训练代码都像下面这条流水线：

```text
Dataset -> DataLoader -> Tensor -> model -> loss -> backward -> optimizer
```

翻译成人话：

```text
准备数据 -> 分批取数据 -> 送进模型 -> 算错多少 -> 算怎么改 -> 更新模型
```

前 14 课其实就是围着这条线一点点拆。

## 第 2 课会先遇到什么

第 2 课只会重点遇到三个东西：

1. `Dataset`：MNIST 这个数据集。
2. `Tensor`：图片被变成张量。
3. `shape`：看张量的形状。

所以读第 2 课时，不需要急着理解 `nn`、`loss`、`optimizer`。那些会在第 5 课以后慢慢出现。

## 最小记忆版

现在只记这几句：

- `torch` 是 PyTorch 的总工具包。
- `Tensor` 是 PyTorch 里的数据。
- `Dataset` 管数据。
- `DataLoader` 分批拿数据。
- `nn` 搭模型。
- `loss` 衡量错多少。
- `optimizer` 负责改参数。

## 本节检查问题

- `Tensor` 可以先理解成什么？
- `Dataset` 和 `DataLoader` 有什么区别？
- `loss` 是告诉模型“预测结果”还是“错得多不多”？
- 第 2 课主要会遇到哪三个东西？

## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 1 课](01-pytorch-installation.md)
- 下一课：[第 2 课](02-mnist-data.md)

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

## Debug 检查

如果模型运行失败，先不要乱改层数。先确认 forward 里哪一步 shape 开始不对。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 20 课](20-dataset-transform-normalization.md)
- 下一课：[第 22 课](22-activation-functions.md)

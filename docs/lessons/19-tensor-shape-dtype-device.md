# PyTorch MNIST 19 Tensor 的 shape、dtype 和 device

> 核心概念：shape、dtype、device

# 第 19 课：先学会看懂 Tensor 的身份证

Tensor 是 PyTorch 里最常见的数据格式。复刻项目和 Debug 时，第一步通常不是改模型，而是确认 Tensor 的三件事：

```text
shape：长什么形状
dtype：里面是什么类型的数字
device：放在 CPU 还是 GPU
```

## shape：数据的形状

MNIST 图片常见形状是：

```text
[batch_size, 1, 28, 28]
```

它表示一批图片、1 个灰度通道、高 28、宽 28。模型报 shape 错误时，先打印输入和输出形状。

## dtype：数字类型

图片通常是 `float32`，标签通常是整数类别。分类任务用 `CrossEntropyLoss` 时，标签一般应该是类别编号，不是 one-hot。

## device：数据在哪

模型和数据必须在同一个设备上。模型在 GPU、数据在 CPU，就会报 device mismatch。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\19_inspect_tensor_metadata.py
```

看到 `Tensor 元数据验证通过`，说明你已经能检查 shape、dtype 和 device。

- 打印一个 batch 的 `images.shape`、`images.dtype`、`images.device`。
- 打印 `labels.shape`、`labels.dtype`、`labels.device`。
- 解释为什么图片和标签的 dtype 不一样。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里怎么看 |
| --- | --- | --- |
| Tensor | PyTorch 里的数字容器 | `images`、`labels` |
| shape | 这个数字容器的尺寸 | `images.shape` |
| dtype | 容器里数字的类型 | `images.dtype` |
| device | Tensor 放在哪里计算 | `images.device` |

## 源码逐段讲解

### 1. 人造一批图片

```python
images = torch.zeros(4, 1, 28, 28, dtype=torch.float32)
```

这行创建了 4 张全黑图片。

`4, 1, 28, 28` 依次表示：

```text
4 张图、1 个灰度通道、高 28、宽 28
```

`dtype=torch.float32` 表示图片像素用小数类型保存。神经网络通常用小数做计算。

### 2. 人造一组标签

```python
labels = torch.tensor([0, 1, 2, 3], dtype=torch.long)
```

标签是类别编号，所以这里是整数。`CrossEntropyLoss` 通常要求分类标签是 `torch.long`。

### 3. 打印 Tensor 的身份证

```python
print(f"图片 shape：{images.shape}")
print(f"图片 dtype：{images.dtype}")
print(f"图片 device：{images.device}")
```

以后遇到 PyTorch 报错，第一反应不是乱改代码，而是先把这三项打印出来。

### 4. 用检查验证理解

```python
if images.shape != (4, 1, 28, 28):
    raise RuntimeError("图片 shape 不符合预期。")
```

这些 `if` 不是为了为难你，而是让脚本自动告诉你：当前 Tensor 是否符合预期。

## 输出怎么读

- `图片 shape：[4, 1, 28, 28]`：4 张灰度图，每张 28x28。
- `图片 dtype：torch.float32`：图片像素是小数。
- `标签 shape：[4]`：4 张图对应 4 个答案。
- `标签 dtype：torch.int64` 或 `torch.long`：分类标签是整数类别编号。
- `device：cpu`：当前数据放在 CPU 上。

## 你真正学到了什么

PyTorch Debug 的第一步通常不是看模型多高级，而是看 Tensor 身份证：

```text
shape 对不对？
dtype 对不对？
device 对不对？
```

很多看起来复杂的报错，本质上都是这三件事之一不匹配。

## 你可以自己改一改

把：

```python
labels = torch.tensor([0, 1, 2, 3], dtype=torch.long)
```

临时改成：

```python
labels = torch.tensor([0, 1, 2, 3], dtype=torch.float32)
```

再运行脚本。你会看到检查报错。这个实验想让你记住：图片可以是小数，但分类标签通常应该是整数类别编号。

## Debug 检查

遇到报错先问：

- 输入 shape 是否符合模型期待？
- labels 是不是类别编号？
- 模型和数据是不是在同一个 device？

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 18 课](18-decision-tree-random-forest.md)
- 下一课：[第 20 课](20-dataset-transform-normalization.md)

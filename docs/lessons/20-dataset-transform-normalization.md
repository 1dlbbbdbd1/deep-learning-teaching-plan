# PyTorch MNIST 20 Dataset、transform 和 normalization

> 核心概念：Dataset、transform、normalize

# 第 20 课：数据进模型前要先整理

模型不是直接吃原始图片。图片通常要经过 transform，变成 Tensor，再做必要的标准化。

```text
原始图片 -> transform -> Tensor -> normalization -> model
```

## Dataset 负责什么

`Dataset` 像一个数据仓库。你问它第 `i` 条数据，它返回：

```text
image, label
```

## transform 负责什么

transform 是数据进模型前的处理流程。MNIST 里最常见的是：

```python
transforms.ToTensor()
```

它会把图片转成 Tensor，并把像素缩放到 0 到 1。

## normalization 是什么

normalization 是把数值分布整理到更适合训练的范围。它不是必须从第一天掌握，但复刻项目时经常会看到。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\20_dataset_transform_normalization.py
```

看到 `Dataset transform normalization 验证通过`，说明你已经能把数据放进 Dataset、DataLoader，并观察标准化效果。

- 找到项目里 `transforms.ToTensor()` 出现的位置。
- 比较 transform 前后的图片表示。
- 记录图片 Tensor 的最小值和最大值。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| Dataset | 能按编号取数据的仓库 | `TensorDataset(...)` |
| DataLoader | 帮你按 batch 取数据的搬运工 | `DataLoader(...)` |
| normalization | 把数字整理到更适合训练的范围 | `(raw_features - mean) / std` |
| mean | 平均值 | `raw_features.mean(dim=0)` |
| std | 标准差，粗略理解为分散程度 | `raw_features.std(dim=0)` |

## 源码逐段讲解

### 1. 准备原始特征

```python
raw_features = torch.tensor(
    [
        [0.0, 10.0],
        [1.0, 11.0],
        ...
    ],
    dtype=torch.float32,
)
```

这里有 4 条样本，每条样本 2 个特征。

第二个特征比第一个特征整体大很多，所以我们用它演示标准化。

### 2. 计算均值和标准差

```python
mean = raw_features.mean(dim=0)
std = raw_features.std(dim=0)
```

`dim=0` 表示“按列算”。也就是分别计算第 1 个特征和第 2 个特征的均值、标准差。

### 3. 做标准化

```python
normalized_features = (raw_features - mean) / std
```

这行可以读成：

```text
先减掉平均水平，再除以分散程度
```

标准化后，数字不会完全一样，但整体会更接近“均值 0、尺度相近”的状态。

### 4. 包成 Dataset

```python
dataset = TensorDataset(normalized_features, labels)
```

`TensorDataset` 会把特征和标签绑在一起。以后取第 0 条数据时，会同时得到第 0 条特征和第 0 个标签。

### 5. 用 DataLoader 取 batch

```python
loader = DataLoader(dataset, batch_size=2, shuffle=False)
batch_features, batch_labels = next(iter(loader))
```

`batch_size=2` 表示一次取 2 条样本。

`shuffle=False` 表示先不打乱，方便学习时观察顺序。

## 输出怎么读

- `原始特征均值`：每个特征列自己的平均值。
- `原始特征标准差`：每个特征列自己的分散程度。
- `标准化后整体均值：0.0000`：标准化大致把数据中心拉回 0。
- `batch 特征 shape：[2, 2]`：一次取 2 条样本，每条 2 个特征。
- `batch 标签 shape：[2]`：这 2 条样本对应 2 个答案。

## 你真正学到了什么

数据进入模型前，通常要经过一条流水线：

```text
原始数据 -> 预处理/标准化 -> Dataset -> DataLoader -> batch -> model
```

以后复刻项目时，别只盯模型文件。数据流水线错了，模型再高级也可能训练不好。

## 你可以自己改一改

把：

```python
loader = DataLoader(dataset, batch_size=2, shuffle=False)
```

临时改成：

```python
loader = DataLoader(dataset, batch_size=4, shuffle=False)
```

再运行脚本。你会看到 `batch 特征 shape` 变成 `[4, 2]`。

这个实验能帮你理解：batch size 改的是“一次喂给模型多少条数据”。

## Debug 检查

如果模型效果很差，检查：

- 训练和测试是否用了同样的 transform。
- 图片数值范围是不是符合预期。
- 数据增强有没有只用于训练集。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 19 课](19-tensor-shape-dtype-device.md)
- 下一课：[第 21 课](21-custom-nn-module.md)

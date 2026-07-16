# PyTorch MNIST 30 复刻数据流

> 核心概念：数据入口、预处理、batch

# 第 30 课：先复刻数据，再复刻模型

项目复刻时，数据流比模型更早检查。

```text
数据文件 -> Dataset -> transform -> DataLoader -> batch
```

## 为什么先看数据

如果数据 shape、标签、预处理错了，模型写对也训练不好。

## 需要记录什么

- 数据从哪里来。
- 每条样本长什么样。
- 标签是什么格式。
- batch 的 shape。
- 训练集和测试集是否分开。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\30_reproduce_data_pipeline.py
```

看到 `复刻数据流验证通过`，说明你已经跑通一个最小 Dataset 到 DataLoader 的数据流。

- 只运行数据加载部分。
- 打印一个 batch 的 shape。
- 打印标签范围。
- 保存一张样本图检查是否正常。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| data pipeline | 数据从文件到 batch 的路线 | `TensorDataset -> DataLoader` |
| sample | 一条样本 | `features` 的一行 |
| label range | 标签最小到最大是多少 | `labels.min()`、`labels.max()` |
| batch | 一次喂给模型的一小批数据 | `batch_features` |

## 源码逐段讲解

### 1. 准备 6 条假特征

```python
features = torch.arange(24, dtype=torch.float32).reshape(6, 4)
```

`torch.arange(24)` 生成 0 到 23 的数字。

`.reshape(6, 4)` 把它整理成：

```text
6 条样本，每条 4 个特征
```

### 2. 准备标签

```python
labels = torch.tensor([0, 0, 1, 1, 2, 2], dtype=torch.long)
```

这里有 3 个类别：0、1、2。

6 个标签必须对应 6 条特征。

### 3. 绑定成 Dataset

```python
dataset = TensorDataset(features, labels)
```

这一步让第 i 条特征和第 i 个标签绑在一起，避免错位。

### 4. 用 DataLoader 取 batch

```python
loader = DataLoader(dataset, batch_size=3, shuffle=False)
batch_features, batch_labels = next(iter(loader))
```

`batch_size=3` 表示第一次会取前 3 条样本。

因为 `shuffle=False`，所以标签应该是 `[0, 0, 1]`。

### 5. 检查标签范围

```python
labels.min().item()
labels.max().item()
```

复刻分类项目时，一定要知道标签范围。比如 10 分类通常标签应该在 `0` 到 `9`。

## 输出怎么读

- `数据集样本数：6`：Dataset 里有 6 条数据。
- `batch 特征 shape：[3, 4]`：一次取 3 条，每条 4 个特征。
- `batch 标签：[0, 0, 1]`：第一批数据的答案。
- `标签范围：0 到 2`：这是 3 分类标签。

## 你真正学到了什么

复刻项目时，先让数据流单独跑通：

```text
Dataset 能取样本吗？
DataLoader 能出 batch 吗？
feature shape 对吗？
label 范围对吗？
训练集和测试集分开了吗？
```

数据流不清楚时，不要急着改模型。

## 你可以自己改一改

把：

```python
batch_size=3
```

临时改成：

```python
batch_size=2
```

再运行脚本。`batch 特征 shape` 会变成 `[2, 4]`，但最后的标签顺序检查也会失败。

这个失败说明：你改了数据流参数，就要同步更新验证条件。

## Debug 检查

如果模型效果离谱，先别骂模型。先查数据有没有读错、归一化有没有不一致、标签有没有错位。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 29 课](29-reproduce-project-readme-env-entry.md)
- 下一课：[第 31 课](31-reproduce-model-loss-training-loop.md)

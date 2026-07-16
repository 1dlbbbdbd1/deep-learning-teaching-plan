# PyTorch MNIST 04 DataLoader 和 Batch

> 核心概念：DataLoader、batch、shape

# 第 4 课：用 DataLoader 批量取样本

这一课真正要解决的是：

```text
训练模型时为什么不是一张一张图片喂进去，而是一次喂一批？
```

## 今天只理解两个词

1. **DataLoader**：PyTorch 用来“按批次取数据”的工具。
2. **batch**：一小批样本。训练神经网络时通常不是一张一张喂，而是一批一批喂。

上一课一张 MNIST 图片的形状是：

```text
torch.Size([1, 28, 28])
```

这一课一次取 32 张图片，所以图片 batch 的形状会变成：

```text
torch.Size([32, 1, 28, 28])
```

这四个数字分别是：

- `32`：这一批里有 32 张图片。
- `1`：每张图片 1 个灰度通道。
- `28`：每张图片高 28 像素。
- `28`：每张图片宽 28 像素。

标签 batch 的形状是：

```text
torch.Size([32])
```

意思是这 32 张图片对应 32 个数字标签。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| DataLoader | 自动从数据仓库里按批取数据的工具 | `train_loader` |
| batch | 一小批样本 | 32 张图片和 32 个标签 |
| batch size | 每批有多少条样本 | `BATCH_SIZE = 32` |
| shuffle | 是否打乱顺序 | `shuffle=False` |

## 源码逐段讲解

### 1. 设置每批数量

```python
BATCH_SIZE = 32
```

这表示每次从训练集中取 32 张图片。

你可以先理解成：模型每次做题不是做 1 道，而是做 32 道。

### 2. 加载 MNIST 并转成 Tensor

```python
train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=False,
    transform=transforms.ToTensor(),
)
```

这里的 `transform=transforms.ToTensor()` 很重要。DataLoader 取出来的图片会直接是 Tensor，后面才能放进模型。

### 3. 创建 DataLoader

```python
train_loader = DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=False,
)
```

这段代码告诉 PyTorch：

- 从 `train_data` 里取数据。
- 每次取 32 条。
- 暂时不打乱顺序。

### 4. 取出第一批

```python
images, labels = next(iter(train_loader))
```

`iter(train_loader)` 可以理解成打开一个取数据的开关。

`next(...)` 表示取出第一批。

取出来的结果仍然是两部分：

```text
images：32 张图片
labels：32 个标准答案
```

## 运行脚本

```powershell
python .\mnist_project\04_inspect_dataloader_batch.py
```

期待看到：

```text
batch size：32
图片 batch 形状：torch.Size([32, 1, 28, 28])
标签 batch 形状：torch.Size([32])
DataLoader batch 验证通过
```

## 输出怎么读

- `图片 batch 形状：[32, 1, 28, 28]`：这批里有 32 张图片，每张是 1 通道、28 高、28 宽。
- `标签 batch 形状：[32]`：这批图片对应 32 个答案。
- `前 10 个标签`：让你看到这一批前几张图片的标准答案。

标签没有 `[1, 28, 28]`，因为标签不是图片。标签只是“这张图是几”。

## 你真正学到了什么

训练神经网络时，数据通常按 batch 流动：

```text
Dataset 里有很多样本
DataLoader 每次取出一个 batch
模型一次处理这个 batch
```

以后看到 `[32, 1, 28, 28]`，不要慌，第一个数字通常就是 batch size。

## 你可以自己改一改

把：

```python
BATCH_SIZE = 32
```

改成：

```python
BATCH_SIZE = 16
```

再运行脚本，观察图片 batch 和标签 batch 的第一个数字是否变成 16。

## 本节检查问题

- `torch.Size([32, 1, 28, 28])` 里多出来的 `32` 表示什么？
- 为什么标签 batch 是 `torch.Size([32])`，而不是 `torch.Size([32, 1, 28, 28])`？
- `DataLoader` 和 `Dataset` 分别负责什么？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 3 课](03-mnist-visualization.md)
- 下一课：[第 5 课](05-minimal-model-forward.md)

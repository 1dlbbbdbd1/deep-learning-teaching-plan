# PyTorch MNIST 35 ViT 的 Encoder 和分类头

> 核心概念：Transformer Encoder、CLS token、分类头

# 第 35 课：把 patch 送进 Transformer

patch embedding 之后，ViT 会把这些向量送进 Transformer Encoder。

```text
patch embeddings -> Transformer Encoder -> classifier
```

## CLS token 是什么

很多 ViT 会加一个特殊 token，用它汇总整张图片的信息。最后分类头读取这个 token 的输出。

## Encoder 做什么

Encoder 会让每个 patch 和其他 patch 交互。它能学习图片不同区域之间的关系。

## 分类头是什么

分类头通常是一个线性层：

```text
embedding -> 10 个 logits
```

MNIST 仍然是 10 分类，所以最后输出还是 `[batch_size, 10]`。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\35_vit_encoder_classifier.py
```

看到 `ViT Encoder 和分类头验证通过`，说明你已经跑通 Transformer Encoder 到分类 logits 的最小流程。

- 写出 Transformer 输入 shape。
- 确认是否有 CLS token。
- 写出分类头输出 shape。
- 用交叉熵计算 loss。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| CLS token | 用来汇总整张图信息的特殊向量 | `cls_token` |
| sequence | patch embedding 排成的一串向量 | `sequence` |
| Encoder | 让 token 之间互相交流的模块 | `nn.TransformerEncoder` |
| classifier | 分类头，把向量变成类别分数 | `nn.Linear(EMBED_DIM, CLASS_COUNT)` |

## 源码逐段讲解

### 1. 准备 patch embeddings

```python
patch_embeddings = torch.randn(BATCH_SIZE, PATCH_COUNT, EMBED_DIM)
```

shape 是 `[2, 16, 8]`：

```text
2 张图，每张 16 个 patch，每个 patch 8 维
```

这相当于接着第 34 课的输出继续往下走。

### 2. 添加 CLS token

```python
cls_token = torch.zeros(BATCH_SIZE, 1, EMBED_DIM)
sequence = torch.cat([cls_token, patch_embeddings], dim=1)
```

CLS token 是额外加在最前面的一个向量。

原来每张图 16 个 patch，加上 CLS 后变成 17 个 token。

所以 `sequence.shape` 是 `[2, 17, 8]`。

### 3. 创建 Transformer Encoder

```python
encoder_layer = nn.TransformerEncoderLayer(
    d_model=EMBED_DIM,
    nhead=2,
    dim_feedforward=32,
    batch_first=True,
)
```

几个参数先这样理解：

- `d_model=8`：每个 token 是 8 维。
- `nhead=2`：注意力分成 2 个头。
- `batch_first=True`：输入 shape 用 `[batch, sequence, embedding]`。

### 4. 取 CLS 输出做分类

```python
encoded = encoder(sequence)
cls_output = encoded[:, 0]
logits = classifier(cls_output)
```

`encoded[:, 0]` 取每张图的第 0 个 token，也就是 CLS token 的输出。

分类头把它变成 10 个类别分数。

## 输出怎么读

- `Transformer 输入 shape：[2, 17, 8]`：2 张图，每张 17 个 token，每个 8 维。
- `CLS 输出 shape：[2, 8]`：每张图得到一个 8 维汇总向量。
- `分类 logits shape：[2, 10]`：每张图输出 10 个类别分数。

## 你真正学到了什么

最小 ViT 分类流程可以先记成：

```text
patch embeddings -> 加 CLS token -> Transformer Encoder -> 取 CLS 输出 -> Linear 分类头
```

遇到 Transformer shape 报错时，先确认是不是 `[batch, sequence, embedding]` 顺序弄错了。

## 你可以自己改一改

把：

```python
CLASS_COUNT = 10
```

临时改成：

```python
CLASS_COUNT = 5
```

再运行脚本。输出 logits 会变成 `[2, 5]`，但这不适合 MNIST，因为 MNIST 是 10 分类。

## Debug 检查

如果 Transformer 报 shape 错，先确认 batch 维、sequence 维和 embedding 维的顺序。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 34 课](34-vit-patch-embedding.md)
- 下一课：[第 36 课](36-final-reproduction-report.md)

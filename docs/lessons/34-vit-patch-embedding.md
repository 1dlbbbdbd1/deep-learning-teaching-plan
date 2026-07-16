# PyTorch MNIST 34 ViT 的 patch embedding

> 核心概念：patch、embedding、position

# 第 34 课：ViT 先把图片切成 patch

ViT 不是从像素点逐个看图片，而是先把图片切成小块。

```text
image -> patches -> patch embeddings
```

## patch 是什么

patch 是图片的小方块。比如把 28x28 的 MNIST 图片切成 7x7 的块，就会得到 16 个 patch。

## embedding 是什么

embedding 是把每个 patch 变成一段向量，方便 Transformer 处理。

## position 为什么需要

Transformer 本身不天然知道顺序。位置编码告诉模型每个 patch 原来在图片哪里。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\34_vit_patch_embedding.py
```

看到 `ViT patch embedding 验证通过`，说明你已经能把图片切成 patch 并投影成 embedding。

- 写出图片 shape。
- 选择 patch size。
- 计算 patch 数量。
- 写出 patch embedding 后的 shape。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| patch | 图片小块 | `PATCH_SIZE = 7` |
| patch count | 一张图切出多少块 | `patches.shape[1]` |
| embedding | 把 patch 变成固定长度向量 | `projection(patches)` |
| sequence | Transformer 要吃的一串向量 | 下一课会继续用 |

## 源码逐段讲解

### 1. 设置 patch 参数

```python
BATCH_SIZE = 2
PATCH_SIZE = 7
EMBED_DIM = 8
```

MNIST 图片是 28x28。patch size 是 7，所以一边能切：

```text
28 / 7 = 4
```

整张图能切：

```text
4 * 4 = 16 个 patch
```

### 2. 造一批图片

```python
images = torch.randn(BATCH_SIZE, 1, 28, 28)
```

shape 是 `[2, 1, 28, 28]`：2 张灰度图。

### 3. 用 unfold 切 patch

```python
patches = images.unfold(2, PATCH_SIZE, PATCH_SIZE).unfold(3, PATCH_SIZE, PATCH_SIZE)
```

`unfold` 可以理解成“按窗口切片”。

第一个 `unfold(2, ...)` 沿高度切，第二个 `unfold(3, ...)` 沿宽度切。

### 4. 整理 patch 形状

```python
patches = patches.contiguous().view(BATCH_SIZE, 1, -1, PATCH_SIZE, PATCH_SIZE)
patches = patches.flatten(3).squeeze(1)
```

整理后 `patches.shape` 应该是：

```text
[2, 16, 49]
```

意思是：

```text
2 张图，每张 16 个 patch，每个 patch 有 7*7=49 个像素
```

### 5. 把 patch 投影成 embedding

```python
projection = nn.Linear(PATCH_SIZE * PATCH_SIZE, EMBED_DIM)
embeddings = projection(patches)
```

每个 49 维 patch 被变成 8 维 embedding。

所以输出是 `[2, 16, 8]`。

## 输出怎么读

- `图片 shape：[2, 1, 28, 28]`：2 张输入图片。
- `patch 数量：16`：每张图切成 16 块。
- `patch embedding shape：[2, 16, 8]`：每个 patch 变成 8 维向量。

## 你真正学到了什么

ViT 的第一步不是卷积，而是把图片变成一串 patch 向量：

```text
图片 -> patch -> flatten patch -> Linear 投影 -> patch embeddings
```

后面的 Transformer 处理的不是原始图片，而是这串 embedding。

## 你可以自己改一改

把：

```python
PATCH_SIZE = 7
```

临时改成：

```python
PATCH_SIZE = 14
```

再运行脚本。你会看到 patch 数量应该从 16 变成 4，但脚本原检查会失败。

这个实验想让你理解：patch size 变了，patch 数量和 shape 检查也必须同步改。

## Debug 检查

ViT 最常见的早期错误是 patch 数量和 embedding shape 算错。每一步都打印 shape。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 33 课](33-common-bug-drills.md)
- 下一课：[第 35 课](35-vit-encoder-classifier.md)

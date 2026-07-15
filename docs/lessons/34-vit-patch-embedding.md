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

## Debug 检查

ViT 最常见的早期错误是 patch 数量和 embedding shape 算错。每一步都打印 shape。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 33 课](33-common-bug-drills.md)
- 下一课：[第 35 课](35-vit-encoder-classifier.md)

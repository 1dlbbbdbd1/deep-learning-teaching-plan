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

## Debug 检查

如果 Transformer 报 shape 错，先确认 batch 维、sequence 维和 embedding 维的顺序。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 34 课](34-vit-patch-embedding.md)
- 下一课：[第 36 课](36-final-reproduction-report.md)

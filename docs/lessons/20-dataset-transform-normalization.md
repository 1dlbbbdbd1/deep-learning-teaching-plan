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

## Debug 检查

如果模型效果很差，检查：

- 训练和测试是否用了同样的 transform。
- 图片数值范围是不是符合预期。
- 数据增强有没有只用于训练集。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 19 课](19-tensor-shape-dtype-device.md)
- 下一课：[第 21 课](21-custom-nn-module.md)

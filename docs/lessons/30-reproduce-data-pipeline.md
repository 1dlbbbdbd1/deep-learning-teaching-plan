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

## Debug 检查

如果模型效果离谱，先别骂模型。先查数据有没有读错、归一化有没有不一致、标签有没有错位。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 29 课](29-reproduce-project-readme-env-entry.md)
- 下一课：[第 31 课](31-reproduce-model-loss-training-loop.md)

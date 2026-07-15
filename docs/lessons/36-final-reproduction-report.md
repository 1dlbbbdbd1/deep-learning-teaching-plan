# PyTorch MNIST 36 最终复刻报告和 Debug 复盘

> 核心概念：复刻报告、证据、回归验证

# 第 36 课：把复刻过程写成报告

最后一课不是再学一个新模型，而是把复刻和 Debug 过程整理成可复查的报告。

## 报告要回答什么

- 复刻了哪个项目。
- 环境怎么准备。
- 数据怎么进入模型。
- 模型结构是什么。
- 训练和评估怎么跑。
- 遇到了哪些错误。
- 每个错误如何复现、定位、修复和验证。

## 推荐结构

```text
项目目标：
运行环境：
数据流：
模型结构：
训练流程：
评估结果：
Debug 记录：
最终结论：
仍然不懂的问题：
```

## 最终验收标准

你不需要成为论文作者，但要做到：

- 能独立跑通项目。
- 能画出数据到模型的流程。
- 能解释主要 shape。
- 能用固定 Debug 流程处理报错。
- 能写出最小复现和回归验证。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\36_final_reproduction_report.py
```

看到 `最终复刻报告验证通过`，说明你已经知道最终报告至少要包含哪些部分。

- 选择一个 CNN 或最小 ViT 项目。
- 跑通原项目。
- 复刻最小版本。
- 整理至少 3 条 Debug 记录。
- 写最终复刻报告。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 35 课](35-vit-encoder-classifier.md)
- Debug 工作流：[Debug 工作流](../debugging/debug-workflow.md)
- Debug 记录模板：[Debug 记录模板](../debugging/debug-record-template.md)

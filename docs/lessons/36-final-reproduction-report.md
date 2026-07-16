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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| reproduction report | 复刻报告，记录你怎么跑通项目 | `report` 字典 |
| evidence | 证据，不是感觉 | Debug 记录 |
| regression verification | 修复后重新跑验证 | “回归验证” |
| unknowns | 仍然不懂的问题 | `仍然不懂的问题` |

## 源码逐段讲解

### 1. 规定报告必须有哪些章节

```python
required_sections = [
    "项目目标",
    "运行环境",
    ...
]
```

这份列表是最终报告的骨架。缺章节就说明复刻过程还没讲清楚。

### 2. 写一份最小报告

```python
report = {
    "项目目标": "复刻一个最小 CNN 或 ViT 分类项目",
    ...
}
```

这里不是写长文，而是示范每个章节至少要回答什么。

比如“数据流”至少要记录：

```text
Dataset、transform、DataLoader、batch shape
```

### 3. 打印报告内容

```python
for section in required_sections:
    print(f"{section}：{report[section]}")
```

这样终端输出会按固定顺序展示报告。

### 4. 检查是否缺章节

```python
missing = [section for section in required_sections if section not in report]
```

如果缺了“Debug 记录”或“评估结果”，脚本会报错。

这和真实复刻一样：没记录证据，就不能算完整复刻。

## 输出怎么读

每一行都是最终报告的一节。

重点不是背模板，而是确保你的复刻过程能被别人复查：

- 环境能复现吗？
- 数据流讲清楚了吗？
- 模型输入输出 shape 写了吗？
- Debug 记录有证据吗？
- 修复后做回归验证了吗？

## 你真正学到了什么

复刻项目的终点不是“我这里跑通了”，而是：

```text
我能说明怎么跑通
我能解释关键 shape
我能记录错误和证据
我能让别人按报告复查
```

这才是从“跟着跑脚本”走向“独立学习”的分界线。

## 你可以自己改一改

从 `report` 字典里临时删掉：

```python
"Debug 记录": ...
```

再运行脚本。它会报错，说明最终报告不能缺 Debug 复盘。

这个实验是在提醒你：复刻项目时，报错记录不是附加项，是必需品。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 35 课](35-vit-encoder-classifier.md)
- Debug 工作流：[Debug 工作流](../debugging/debug-workflow.md)
- Debug 记录模板：[Debug 记录模板](../debugging/debug-record-template.md)

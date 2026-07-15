# PyTorch MNIST 32 Debug 工作流实战

> 核心概念：复现、缩小、假设、证据、修复、回归

# 第 32 课：Debug 不是乱试

固定流程：

```text
复现问题 -> 缩小输入 -> 提出假设 -> 增加证据 -> 最小修复 -> 回归验证
```

## 复现问题

先把错误稳定跑出来。不能稳定复现，就很难判断修复是否有效。

## 缩小输入

把完整训练缩小成一个 batch，甚至一张图片。输入越小，问题越清楚。

## 提出假设

不要同时改很多地方。一次只验证一个猜测。

## 增加证据

证据可以是：

- shape 打印。
- dtype 打印。
- device 打印。
- loss 数值。
- 梯度是否为 None。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\32_debug_workflow_practice.py
```

看到 `Debug 工作流实战验证通过`，说明你已经看过一次 shape 错误如何被复现、取证和修复。

- 找一个真实报错。
- 写下最小复现命令。
- 写下 2 个可能原因。
- 用打印或断点验证其中一个。
- 修复后再跑原命令。

## Debug 检查

修复后必须回归验证。只跑最小例子不够，还要跑回原来的训练或测试入口。

## 相关链接

- 索引：[课程索引](../course-index.md)
- Debug 工作流：[Debug 工作流](../debugging/debug-workflow.md)
- 上一课：[第 31 课](31-reproduce-model-loss-training-loop.md)
- 下一课：[第 33 课](33-common-bug-drills.md)

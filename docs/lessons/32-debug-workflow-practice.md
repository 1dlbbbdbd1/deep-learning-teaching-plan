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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| reproduce | 让错误稳定出现 | `model(bad_input)` |
| evidence | 证明问题在哪的证据 | `evidence` 字典 |
| hypothesis | 猜测原因 | “输入特征数不匹配” |
| regression test | 修完后重新验证 | `fixed_output` 检查 |

## 源码逐段讲解

### 1. 先列出 Debug 流程

```python
workflow = ["复现问题", "缩小输入", "提出假设", "增加证据", "最小修复", "回归验证"]
```

这不是装饰。以后真遇到报错，就按这个顺序走，避免乱改。

### 2. 故意制造 shape 错误

```python
bad_input = torch.randn(2, 3)
model = nn.Linear(4, 2)
```

模型期待每条样本有 4 个特征，但 `bad_input` 只有 3 个特征。

这会触发典型的矩阵乘法 shape 错误。

### 3. 捕获错误并记录证据

```python
try:
    model(bad_input)
except RuntimeError as error:
    evidence = {
        "输入 shape": tuple(bad_input.shape),
        "模型期待 in_features": model.in_features,
        ...
    }
```

注意：这里不是只复制报错，而是记录能解释问题的证据。

### 4. 做最小修复

```python
fixed_input = torch.randn(2, 4)
fixed_output = model(fixed_input)
```

修复方式是让输入特征数从 3 变成 4，和模型期待一致。

### 5. 回归验证

```python
if fixed_output.shape != (2, 2):
    raise RuntimeError(...)
```

修复后必须验证输出 shape 对不对。否则只是“没报错”，不等于“修对了”。

## 输出怎么读

- `Debug 流程`：提醒你排错顺序。
- `证据`：包含输入 shape、模型期待输入数、错误片段。
- `修复后输出 shape：[2, 2]`：2 条样本，每条输出 2 个类别分数。

## 你真正学到了什么

Debug 的核心不是多试几次，而是把问题变小、把证据变清楚。

遇到 shape 报错时，最小证据通常是：

```text
输入 shape
模型期待 shape
报错第一行
修复后 shape
```

## 你可以自己改一改

把：

```python
fixed_input = torch.randn(2, 4)
```

临时改成：

```python
fixed_input = torch.randn(2, 5)
```

再运行脚本。你会再次得到 shape 错误。

这个实验想让你练习：修复不是随便改一个数字，而是改到和模型期待一致。

## Debug 检查

修复后必须回归验证。只跑最小例子不够，还要跑回原来的训练或测试入口。

## 相关链接

- 索引：[课程索引](../course-index.md)
- Debug 工作流：[Debug 工作流](../debugging/debug-workflow.md)
- 上一课：[第 31 课](31-reproduce-model-loss-training-loop.md)
- 下一课：[第 33 课](33-common-bug-drills.md)

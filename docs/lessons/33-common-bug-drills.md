# PyTorch MNIST 33 常见错误专项训练

> 核心概念：路径、shape、dtype、device、梯度、模式

# 第 33 课：故意制造错误，再修掉

想学会 Debug，不能只等错误出现。要故意制造常见错误，然后按流程修复。

## 常见错误清单

- 解释器错了。
- 路径错了。
- shape 不匹配。
- dtype 不符合 loss 要求。
- CPU/GPU device 不一致。
- 忘了 `zero_grad()`。
- 忘了 `backward()`。
- 忘了 `optimizer.step()`。
- 评估时忘了 `model.eval()`。

## 每个错误都这样记录

```text
现象：
最小复现：
猜测：
证据：
根因：
修复：
回归验证：
```

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\33_common_bug_drills.py
```

看到 `常见错误专项训练验证通过`，说明你已经有一份常见错误排查清单。

- 人为改错一个 shape。
- 人为制造一次 dtype 错误。
- 人为制造一次 device 错误。
- 每个错误都写 Debug 记录。

## 先把术语翻译成人话

| 错误类型 | 人话解释 | 先查什么 |
| --- | --- | --- |
| 路径错误 | 文件找不到、工作目录不对 | `pwd`、文件是否存在 |
| shape 错误 | 数据尺寸和模型期待不一致 | 输入/输出 shape |
| dtype 错误 | 数字类型不符合要求 | 图片 float、标签 long |
| device 错误 | CPU/GPU 放得不一致 | 模型和数据 device |
| 梯度错误 | 参数没有正确学习 | zero_grad/backward/step |
| 模式错误 | 训练/评估模式混了 | train/eval/no_grad |

## 源码逐段讲解

### 1. 用列表保存错误清单

```python
bug_drills = [
    ("路径错误", "确认 cwd 和文件是否存在"),
    ...
]
```

每一项都有两个部分：

```text
错误名字 + 第一检查动作
```

### 2. 打印每个排查动作

```python
for name, check in bug_drills:
    print(f"{name}：{check}")
```

这让你在终端里看到一份最小 Debug 提醒。

### 3. 检查清单数量

```python
if len(bug_drills) != 6:
    raise RuntimeError(...)
```

课程脚本不只是输出文字，还会确认清单没有漏项。

### 4. 检查清单内容

```python
required = {"路径错误", "shape 错误", ...}
actual = {name for name, _ in bug_drills}
```

集合比较可以检查“该有的错误类型是否都在”。

## 输出怎么读

每一行都是一个“遇到问题时先查什么”的提醒。

比如：

```text
shape 错误：打印输入、输出和 Linear/Conv2d 期待的 shape
```

意思是：不要先改模型，先收集 shape 证据。

## 你真正学到了什么

Debug 可以训练，不一定要等项目崩了才学。

你应该建立自己的错误清单。每次遇到新错误，就补充：

```text
现象是什么？
第一检查动作是什么？
最后根因是什么？
```

## 你可以自己改一改

在 `bug_drills` 里新增一项：

```python
("随机性错误", "固定 random seed 后重新运行")
```

再运行脚本。你会发现数量检查失败。

这说明脚本的验证条件也要跟着清单更新。真实项目里，新增功能也要同步更新测试。

## Debug 检查

不要只写“解决了”。必须写清楚证据是什么，为什么这个修复有效。

## 相关链接

- 索引：[课程索引](../course-index.md)
- Debug 记录模板：[Debug 记录模板](../debugging/debug-record-template.md)
- 上一课：[第 32 课](32-debug-workflow-practice.md)
- 下一课：[第 34 课](34-vit-patch-embedding.md)

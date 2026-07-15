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

## Debug 检查

不要只写“解决了”。必须写清楚证据是什么，为什么这个修复有效。

## 相关链接

- 索引：[课程索引](../course-index.md)
- Debug 记录模板：[Debug 记录模板](../debugging/debug-record-template.md)
- 上一课：[第 32 课](32-debug-workflow-practice.md)
- 下一课：[第 34 课](34-vit-patch-embedding.md)

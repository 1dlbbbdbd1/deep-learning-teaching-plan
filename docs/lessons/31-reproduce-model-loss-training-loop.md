# PyTorch MNIST 31 复刻模型、loss 和训练循环

> 核心概念：模型结构、loss、training loop

# 第 31 课：复刻训练闭环

数据流确认后，再复刻模型和训练循环。

顺序是：

```text
模型 forward -> loss -> backward -> optimizer -> eval
```

## 先复刻最小模型

不要一开始就完整搬运复杂项目。先写一个能吃同样 batch、输出同样类别数的最小模型。

## loss 要和任务匹配

分类常用交叉熵。回归常用 MSE。loss 选错，训练会很奇怪。

## 训练循环要逐步确认

每一步都可以打印证据：

- logits shape。
- loss 数值。
- 梯度是否存在。
- 参数是否更新。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\31_reproduce_model_loss_training_loop.py
```

看到 `复刻训练闭环验证通过`，说明你已经验证过 forward、loss、backward 和 step 会让参数更新。

- 写出模型输入输出 shape。
- 跑一个 batch。
- 跑 5 个 batch。
- 跑 1 个 epoch。
- 评估一次。

## Debug 检查

如果 loss 不变，检查是否忘了 `zero_grad()`、`backward()` 或 `optimizer.step()`。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 30 课](30-reproduce-data-pipeline.md)
- 下一课：[第 32 课](32-debug-workflow-practice.md)

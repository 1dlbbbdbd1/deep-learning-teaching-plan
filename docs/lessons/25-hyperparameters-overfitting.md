# PyTorch MNIST 25 学习率、batch size、epoch 和过拟合

> 核心概念：learning rate、batch size、epoch、overfitting

# 第 25 课：训练效果差不一定是模型写错了

很多训练问题来自超参数，而不是代码语法。

常见超参数：

- learning rate：每次参数改多大。
- batch size：每次喂多少样本。
- epoch：完整看几遍训练集。

## 学习率太大或太小

学习率太大，loss 可能震荡甚至爆掉。学习率太小，loss 下降很慢。

## batch size 的影响

batch size 大，训练更稳但可能更占显存。batch size 小，波动更明显。

## 过拟合是什么

训练集越来越好，测试集不提升甚至变差，就是过拟合的常见信号。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\25_hyperparameters_overfitting_demo.py
```

看到 `超参数和过拟合演示验证通过`，说明你已经比较过不同学习率对 loss 的影响。

- 分别记录训练 loss 和测试 accuracy。
- 改一次 learning rate，观察变化。
- 改一次 batch size，观察变化。

## Debug 检查

不要只看最后一个数字。记录趋势比盯着某一次输出更可靠。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 24 课](24-train-mnist-mlp.md)
- 下一课：[第 26 课](26-convolution-feature-map.md)

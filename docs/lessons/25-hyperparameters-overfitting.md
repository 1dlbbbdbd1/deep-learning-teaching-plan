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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| learning rate | 每次参数更新迈多大一步 | `train_with_learning_rate(0.05)` |
| batch size | 一次喂给模型多少样本 | 本课概念解释 |
| epoch | 完整看完整个训练集几遍 | 本课概念解释 |
| overfitting | 训练集好、测试集差 | 本课概念解释 |

## 源码逐段讲解

### 1. 把训练过程封装成函数

```python
def train_with_learning_rate(learning_rate):
```

函数的输入是学习率，输出是训练前后的 loss。这样就能公平比较不同学习率。

### 2. 准备一个小回归任务

```python
x = torch.tensor([[-1.0], [0.0], [1.0], [2.0]])
y = 3 * x - 1
```

目标公式是：

```text
y = 3x - 1
```

模型要学到接近 `w=3`、`b=-1`。

### 3. 把学习率交给优化器

```python
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

`lr` 就是 learning rate。它控制每次 `optimizer.step()` 改参数时迈多大一步。

### 4. 对比小学习率和合适学习率

```python
slow_initial, slow_final = train_with_learning_rate(0.001)
good_initial, good_final = train_with_learning_rate(0.05)
```

两个模型的训练代码一样，主要差别只有学习率。

如果学习率太小，训练 80 步后 loss 可能还比较高。

## 输出怎么读

- `小学习率初始 loss`：学习前的错误程度。
- `小学习率最终 loss`：学习率很小时训练后的错误程度。
- `合适学习率最终 loss`：学习率合适时训练后的错误程度。
- `合适学习率是否下降更多：True`：说明学习率影响训练速度。

## 你真正学到了什么

训练效果不好，不一定是模型结构错了。学习率、batch size、epoch 这些超参数也会明显影响结果。

Debug 训练问题时，先记录趋势：

```text
loss 是下降、震荡，还是爆掉？
accuracy 是提升、停住，还是训练集好测试集差？
```

## 你可以自己改一改

把：

```python
good_initial, good_final = train_with_learning_rate(0.05)
```

临时改成：

```python
good_initial, good_final = train_with_learning_rate(1.0)
```

再运行脚本。你可能会看到训练不稳定或验证失败。

这个实验想让你理解：学习率不是越大越好。

## Debug 检查

不要只看最后一个数字。记录趋势比盯着某一次输出更可靠。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 24 课](24-train-mnist-mlp.md)
- 下一课：[第 26 课](26-convolution-feature-map.md)

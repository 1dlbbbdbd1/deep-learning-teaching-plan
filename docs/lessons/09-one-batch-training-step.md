# PyTorch MNIST 09 一次完整训练步骤

> 核心概念：forward、loss、zero_grad、backward、step

# 第 9 课：完成一次最小训练步骤

这一课真正要解决的是：

```text
把 forward、loss、backward、step 连起来以后，模型是不是真的会往更好的方向动一下？
```

## 今天只理解一件事

训练不是一句神秘咒语，它其实是几句代码按顺序排队：

```python
scores = model(images)
loss = loss_function(scores, labels)
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

可以把它想成：

```text
模型先猜一次 -> 算错多少 -> 清空旧梯度 -> 计算新梯度 -> 更新参数
```

## 为什么还要再算一次 loss

这一课里，我们训练前算一次 loss，更新参数后对同一个 batch 再算一次 loss。

如果训练步骤起作用，通常会看到：

```text
训练后 loss < 训练前 loss
```

这说明模型刚刚往“少错一点”的方向走了一小步。

## 先把五行代码翻译成人话

| 代码 | 人话解释 |
| --- | --- |
| `scores = model(images)` | 模型先做题，输出 10 个分数 |
| `loss = loss_function(scores, labels)` | 对答案，算错得多不多 |
| `optimizer.zero_grad()` | 擦掉上一轮草稿 |
| `loss.backward()` | 根据错误计算怎么改 |
| `optimizer.step()` | 真正改模型参数 |

## 源码逐段讲解

### 1. 先算训练前 loss

```python
scores_before = model(images)
loss_before = loss_function(scores_before, labels)
```

这一步是记录模型还没更新前，在同一批图片上的表现。

### 2. 做一次训练步骤

```python
optimizer.zero_grad()
loss_before.backward()
optimizer.step()
```

这三行合起来，就是最小训练步骤。

### 3. 再算训练后 loss

```python
scores_after = model(images)
loss_after = loss_function(scores_after, labels)
```

为了证明刚才那一步有用，脚本对同一个 batch 再算一次 loss。

如果训练步骤有效，通常 `loss_after` 会小于 `loss_before`。

## 运行脚本

```powershell
python .\mnist_project\09_one_batch_training_step.py
```

期待看到：

```text
训练前 loss：...
训练后 loss：...
同一个 batch 的 loss 是否下降：True
一次训练步骤验证通过
```

## 输出怎么读

- `训练前 loss`：参数更新前，这批图片错得多不多。
- `训练后 loss`：参数更新后，对同一批图片再算一次。
- `是否下降：True`：说明这一步参数更新确实让模型在这批数据上变好了一点。

这不是说模型已经学会 MNIST，只说明“一次训练步骤”这套流程是有效的。

## 你真正学到了什么

从这一课开始，训练不再是抽象词，而是一组固定顺序的动作：

```text
猜一次 -> 算错误 -> 清旧梯度 -> 算新梯度 -> 改参数
```

以后你看到训练代码，先不要被文件名和类名吓住，先找这五件事有没有出现：

1. forward：模型是否算出了输出？
2. loss：有没有把输出和答案比较？
3. zero_grad：有没有清空旧梯度？
4. backward：有没有根据 loss 算梯度？
5. step：有没有真正更新参数？

能找到这五件事，你就能读懂大多数 PyTorch 训练循环的骨架。

## 你可以自己改一改

把：

```python
optimizer.step()
```

临时注释掉，再运行脚本。你会发现训练后 loss 不会正常下降，因为参数没有被更新。

## 本节检查问题

- `optimizer.zero_grad()` 为什么要放在 `backward()` 前面？
- `loss.backward()` 和 `optimizer.step()` 谁负责算梯度，谁负责改参数？
- 为什么这节只检查同一个 batch，而不是整个训练集？
- 为什么 loss 下降只能说明这一个 batch 上变好了？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 8 课](08-optimizer-step.md)
- 下一课：[第 10 课](10-mini-training-loop.md)

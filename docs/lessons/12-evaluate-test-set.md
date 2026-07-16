# PyTorch MNIST 12 测试集准确率

> 核心概念：accuracy、eval、no_grad

# 第 12 课：在测试集上评估准确率

这一课真正要解决的是：

```text
训练 loss 下降不等于模型真的会了，我们还要用没训练过的数据考试。
```

## 今天只理解一个词：accuracy

`accuracy` 就是准确率：

```text
准确率 = 猜对的数量 / 总数量
```

MNIST 测试集有 10000 张图。如果模型猜对 8800 张：

```text
accuracy = 8800 / 10000 = 88%
```

## 训练集和测试集的区别

训练集像练习题，模型可以看答案、根据错误修改参数。

测试集像考试题，模型只能作答，不能再改参数。

所以代码结构是：

```text
训练集：forward -> loss -> backward -> step
测试集：forward -> argmax -> 数猜对几个
```

## 两个先认识、暂时不死磕的 API

```python
model.eval()
```

意思是把模型切到“考试模式”。

```python
with torch.no_grad():
```

意思是考试时不需要算梯度，因为我们不更新参数。

## 源码逐段讲解

### 1. 分别加载训练集和测试集

```python
train=True
train=False
```

`train=True` 是训练集，模型可以用它学习。

`train=False` 是测试集，只用来考试。

### 2. 训练阶段

```python
model.train()
```

这表示模型进入训练模式。

训练阶段仍然执行：

```text
forward -> loss -> backward -> step
```

### 3. 评估阶段

```python
model.eval()
with torch.no_grad():
```

评估阶段不更新参数，所以不需要梯度。

### 4. 从分数变成预测类别

```python
predictions = scores.argmax(dim=1)
```

模型每张图片输出 10 个分数。`argmax(dim=1)` 找出每张图片最高分的位置，这个位置就是预测数字。

### 5. 统计猜对数量

```python
correct_count += (predictions == labels).sum().item()
```

`predictions == labels` 会得到一串 True/False。

`sum()` 会数出猜对了多少个。

## 运行脚本

```powershell
python .\mnist_project\12_evaluate_test_set.py
```

期待看到：

```text
测试样本数：10000
预测正确数：...
测试集准确率：...%
测试集准确率验证通过
```

## 输出怎么读

- `训练样本数：60000`：模型用这些样本学习。
- `测试样本数：10000`：模型用这些样本考试。
- `预测正确数`：10000 张测试图里猜对多少张。
- `测试集准确率`：猜对比例。

这比只看训练 loss 更有意义，因为测试集是模型训练时没用来更新参数的数据。

## 你真正学到了什么

训练和评估是两种不同状态：

```text
训练：允许改参数
评估：只看表现，不改参数
```

如果用测试集继续训练，考试就变成偷看答案了。

## 你可以自己改一改

把：

```python
MIN_EXPECTED_ACCURACY = 85.0
```

改成：

```python
MIN_EXPECTED_ACCURACY = 95.0
```

再运行脚本，观察是否会报错。这个实验能帮你理解“验证阈值”只是我们设定的最低要求。

## 本节检查问题

- 为什么测试集不能拿来训练？
- `argmax(dim=1)` 是从 10 个数字分数里取什么？
- 准确率和 loss 分别在回答什么问题？
- `model.eval()` 和 `torch.no_grad()` 为什么常常一起出现？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 11 课](11-one-epoch-training.md)
- 下一课：[第 13 课](13-save-trained-model.md)

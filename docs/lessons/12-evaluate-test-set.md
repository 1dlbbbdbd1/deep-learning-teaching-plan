# PyTorch MNIST 12 测试集准确率

> 核心概念：accuracy、eval、no_grad

# 第 12 课：在测试集上评估准确率

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

## 本节检查问题

- 为什么测试集不能拿来训练？
- `argmax(dim=1)` 是从 10 个数字分数里取什么？
- 准确率和 loss 分别在回答什么问题？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 11 课](11-one-epoch-training.md)
- 下一课：[第 13 课](13-save-trained-model.md)

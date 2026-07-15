# PyTorch MNIST 28 训练和评估 MNIST CNN

> 核心概念：CNN 训练、eval、保存加载

# 第 28 课：CNN 也要完成训练闭环

CNN 的训练循环和 MLP 一样，变的是模型结构，不变的是训练流程。

```text
DataLoader -> CNN -> loss -> backward -> optimizer -> eval
```

## 先做最小版本

不要一开始就堆很多层。先让一个小 CNN 跑通，再逐步加复杂度。

## 评估时要切换模式

训练时：

```python
model.train()
```

评估时：

```python
model.eval()
```

并配合 `torch.no_grad()`。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\28_train_evaluate_cnn_toy.py
```

看到 `CNN 玩具训练评估验证通过`，说明你已经跑过一个很小的 CNN 训练和评估闭环。

- 训练一个最小 CNN。
- 记录训练 loss。
- 记录测试 accuracy。
- 保存并加载模型。
- 用同一张图片确认加载后预测一致。

## Debug 检查

如果 CNN 没比线性模型好，不要急着改架构。先确认 transform、shape、loss、学习率和 eval 模式。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 27 课](27-pooling-channels-cnn.md)
- 下一课：[第 29 课](29-reproduce-project-readme-env-entry.md)

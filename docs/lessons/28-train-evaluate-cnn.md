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

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| CNN | 用卷积处理图片的网络 | `nn.Conv2d(...)` |
| train mode | 训练模式 | `model.train()` |
| eval mode | 评估模式 | `model.eval()` |
| toy task | 小到能看懂的练习任务 | 左上亮块/右下亮块 |

## 源码逐段讲解

### 1. 造一个 CNN 玩具任务

```python
images = torch.zeros(8, 1, 28, 28)
labels = torch.tensor([0, 1, 0, 1, 0, 1, 0, 1], dtype=torch.long)
images[labels == 0, :, 6:14, 6:14] = 1.0
images[labels == 1, :, 14:22, 14:22] = 1.0
```

标签为 `0` 的图片左上角亮，标签为 `1` 的图片右下角亮。

这个任务不是完整 MNIST，只是为了让 CNN 快速学会一个空间位置规律。

### 2. 定义 CNN

```python
nn.Conv2d(1, 4, kernel_size=3)
nn.ReLU()
nn.MaxPool2d(2)
nn.Flatten()
nn.Linear(4 * 13 * 13, 10)
```

这和第 27 课的最小 CNN 一样，只是这次真的训练它。

### 3. 训练前记录 loss

```python
initial_loss = loss_function(model(images), labels).item()
```

没有这个初始值，你就不知道训练后有没有变好。

### 4. 训练时切到 train 模式

```python
model.train()
```

本课模型里没有 dropout/batchnorm，但先养成习惯。真实项目里训练和评估模式很重要。

### 5. 评估时切到 eval 模式

```python
model.eval()
with torch.no_grad():
```

评估阶段不更新参数，所以用 `no_grad()` 节省计算，也避免误算梯度。

## 输出怎么读

- `任务：用 CNN 区分左上亮块和右下亮块`：玩具分类任务。
- `初始 loss`：训练前错误程度。
- `最终 loss`：训练后应该下降。
- `训练集准确率：1.00`：8 张玩具图片全部分对。

## 你真正学到了什么

CNN 的训练流程没有新魔法：

```text
数据 -> CNN -> loss -> backward -> optimizer.step -> eval
```

模型结构变了，但 Debug 链条仍然可以一步步查。

## 你可以自己改一改

把：

```python
for _ in range(80):
```

临时改成：

```python
for _ in range(5):
```

再运行脚本。训练可能不够充分，准确率或 loss 检查可能失败。

这个实验想让你理解：模型需要足够的更新次数才能学会规律。

## Debug 检查

如果 CNN 没比线性模型好，不要急着改架构。先确认 transform、shape、loss、学习率和 eval 模式。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 27 课](27-pooling-channels-cnn.md)
- 下一课：[第 29 课](29-reproduce-project-readme-env-entry.md)

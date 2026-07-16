# PyTorch MNIST 24 训练一个 MNIST MLP

> 核心概念：训练循环、评估、保存

# 第 24 课：MLP 也要跑完整闭环

升级模型后，训练流程不需要推倒重来。仍然是：

```text
forward -> loss -> zero_grad -> backward -> step -> eval
```

## 训练时关注什么

先看三件事：

- loss 是否整体下降。
- 测试集 accuracy 是否高于线性模型。
- 保存和加载后预测是否一致。

## 不要急着追高分

这一课目标不是刷排行榜，而是确认你能把模型换成 MLP 后仍然跑通完整闭环。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\24_train_mnist_mlp_toy.py
```

看到 `MNIST MLP 玩具训练验证通过`，说明你已经跑过一个很小的 MLP 训练闭环。

- 把线性模型替换成 MLP。
- 训练 1 个 epoch。
- 测试 accuracy。
- 保存 `state_dict`。
- 重新加载并预测一张图片。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| toy task | 玩具任务，故意做得很小方便观察 | 左亮块/右亮块分类 |
| Adam | 一种常用优化器 | `torch.optim.Adam(...)` |
| training steps | 参数更新多少次 | `TRAINING_STEPS = 120` |
| accuracy | 预测正确比例 | `(final_logits.argmax(...) == labels)` |

## 源码逐段讲解

### 1. 造一个玩具图片分类任务

```python
images = torch.zeros(BATCH_SIZE, 1, 28, 28)
labels = torch.tensor([0, 1, 0, 1, 0, 1, 0, 1], dtype=torch.long)
images[labels == 0, :, 8:20, 4:10] = 1.0
images[labels == 1, :, 8:20, 18:24] = 1.0
```

这段代码造了 8 张假图片：

- 标签为 `0` 的图片，左边有亮块。
- 标签为 `1` 的图片，右边有亮块。

这比真实 MNIST 简单很多，目的是让你看清楚 MLP 能不能学到一个明确规律。

### 2. 定义 MLP

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 32),
    nn.ReLU(),
    nn.Linear(32, 10),
)
```

虽然任务只有 0/1 两类，但输出仍然设成 10 类，是为了保持和 MNIST 分类形式一致。

### 3. 记录训练前 loss

```python
with torch.no_grad():
    initial_loss = loss_function(model(images), labels).item()
```

训练前先测一次，后面才能比较模型有没有变好。

### 4. 训练 120 步

```python
for _ in range(TRAINING_STEPS):
    logits = model(images)
    loss = loss_function(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

这依然是熟悉的训练五步。不要被 MLP 吓到，训练骨架没变。

### 5. 计算最终准确率

```python
accuracy = (final_logits.argmax(dim=1) == labels).float().mean().item()
```

拆开读：

```text
argmax 得到预测类别
和 labels 比较得到 True/False
转成 1/0
求平均得到准确率
```

## 输出怎么读

- `任务：用 MLP 区分左侧亮块和右侧亮块`：这不是完整 MNIST，只是玩具任务。
- `初始 loss`：训练前错多少。
- `最终 loss`：训练后应该更低。
- `训练集准确率：1.00`：这 8 张玩具图片都分对了。

## 你真正学到了什么

换成 MLP 后，训练主流程没有变：

```text
forward -> loss -> zero_grad -> backward -> step -> eval
```

模型结构可以变复杂，但你 Debug 时仍然可以沿着这条链条逐步检查。

## 你可以自己改一改

把：

```python
TRAINING_STEPS = 120
```

临时改成：

```python
TRAINING_STEPS = 5
```

再运行脚本。模型可能学不充分，loss 下降不够或准确率不达标。

这个实验想让你理解：训练步数太少，模型可能还没来得及学会。

## Debug 检查

如果训练很慢，先减小 hidden size 或 batch 数量。如果 accuracy 异常低，先确认 labels、loss 和训练模式。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 23 课](23-mlp-forward.md)
- 下一课：[第 25 课](25-hyperparameters-overfitting.md)

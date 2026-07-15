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

## Debug 检查

如果训练很慢，先减小 hidden size 或 batch 数量。如果 accuracy 异常低，先确认 labels、loss 和训练模式。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 23 课](23-mlp-forward.md)
- 下一课：[第 25 课](25-hyperparameters-overfitting.md)

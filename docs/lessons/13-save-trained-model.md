# PyTorch MNIST 13 保存训练好的模型

> 核心概念：state_dict、torch.save

# 第 13 课：保存训练好的模型

## 今天只理解一个词：state_dict

模型训练完以后，真正学到的东西在参数里。

在 PyTorch 里，模型参数通常放在：

```python
model.state_dict()
```

可以把它理解成：

```text
state_dict = 模型里面所有可学习参数的字典
```

我们这个最小线性模型里，最重要的是：

```text
1.weight -> 形状是 (10, 784)
1.bias   -> 形状是 (10,)
```

## 为什么要保存

如果不保存，脚本结束后，训练出来的参数就没了。

保存后，下一课就可以重新加载这个文件，让模型不用重新训练也能预测。

## 运行脚本

```powershell
python .\mnist_project\13_save_trained_model.py
```

期待看到：

```text
保存路径：...\models\mnist_linear_state_dict.pt
权重形状：(10, 784)
偏置形状：(10,)
模型保存验证通过
```

## 文件会不会被 Git 收进去

不会。`models/` 已经写在 `.gitignore` 里。

模型文件是训练产物，不是源码；以后可以重新训练生成。

## 本节检查问题

- `state_dict` 里保存的是代码，还是参数？
- 为什么 `1.weight` 的形状是 `(10, 784)`？
- 为什么训练产物通常不放进 Git？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 12 课](12-evaluate-test-set.md)
- 下一课：[第 14 课](14-load-model-and-predict.md)

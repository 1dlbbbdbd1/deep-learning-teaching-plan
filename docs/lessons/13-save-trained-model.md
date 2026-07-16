# PyTorch MNIST 13 保存训练好的模型

> 核心概念：state_dict、torch.save

# 第 13 课：保存训练好的模型

这一课真正要解决的是：

```text
模型训练完以后，学到的东西怎么留下来，下次不用重新训练？
```

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

## 源码逐段讲解

### 1. 准备保存目录和文件名

```python
models_dir = project_root / "models"
model_path = models_dir / "mnist_linear_state_dict.pt"
```

`models` 目录用来放模型文件。

`.pt` 是 PyTorch 常见的模型参数文件后缀。

### 2. 先训练模型

脚本前半部分和前面一样：训练 1 个 epoch，让线性模型学到参数。

### 3. 创建目录并保存参数

```python
models_dir.mkdir(exist_ok=True)
torch.save(model.state_dict(), model_path)
```

`model.state_dict()` 取出模型参数。

`torch.save(...)` 把参数写入文件。

### 4. 读回来检查

```python
saved_state_dict = torch.load(model_path, map_location="cpu")
```

脚本保存后又读回来，是为了确认文件真的能被 PyTorch 加载。

`map_location="cpu"` 表示先把参数加载到 CPU，避免不同机器 GPU 环境不一致。

## 本节检查问题

- `state_dict` 里保存的是代码，还是参数？
- 为什么 `1.weight` 的形状是 `(10, 784)`？
- 为什么训练产物通常不放进 Git？
- 为什么保存后还要再加载一次检查？

## 输出怎么读

- `保存路径`：模型参数文件放在哪里。
- `模型文件大小`：说明确实写出了一个文件。
- `权重形状：(10, 784)`：线性层从 784 个输入连到 10 个输出。
- `偏置形状：(10,)`：10 个类别各有一个偏置。

## 你真正学到了什么

保存模型通常不是保存整段 Python 代码，而是保存训练出来的参数。

下次只要重新创建同样结构的模型，再把参数加载进去，就能继续使用。

## 你可以自己改一改

把保存文件名临时改成：

```python
model_path = models_dir / "my_first_mnist_model.pt"
```

再运行脚本。你会看到 `models/` 目录下生成一个新文件。

这个实验想让你记住：文件名不神秘，`.pt` 文件本质上就是 PyTorch 保存下来的参数数据。真正重要的是，加载时模型结构必须和保存时一致。


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 12 课](12-evaluate-test-set.md)
- 下一课：[第 14 课](14-load-model-and-predict.md)

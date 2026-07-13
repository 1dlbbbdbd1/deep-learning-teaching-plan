# PyTorch MNIST 14 加载模型并预测单张图片

> 核心概念：load_state_dict、unsqueeze、argmax

# 第 14 课：加载模型并预测单张图片

## 今天完成闭环

这一课把前面的东西串起来：

```text
训练模型 -> 保存参数 -> 重新加载参数 -> 预测一张图片
```

这就是一个最小版手写数字识别程序。

## 加载参数

上一课保存的是：

```python
model.state_dict()
```

这一课加载回来：

```python
state_dict = torch.load(model_path, map_location="cpu")
model.load_state_dict(state_dict)
```

注意：加载参数之前，要先创建同样结构的模型。

## 为什么要 unsqueeze

MNIST 单张图片形状是：

```text
torch.Size([1, 28, 28])
```

模型习惯吃 batch，所以我们把它变成：

```text
torch.Size([1, 1, 28, 28])
```

代码是：

```python
single_image_batch = image.unsqueeze(0)
```

## 为什么用 argmax

模型输出 10 个分数，分别对应数字 0 到 9。

```python
prediction = scores.argmax(dim=1).item()
```

意思是：找出最高分的位置，这个位置就是预测的数字。

## 运行脚本

```powershell
python .\mnist_project\14_load_model_and_predict.py
```

期待看到：

```text
真实标签：7
预测结果：7
是否预测正确：True
单张图片预测验证通过
```

## 本节检查问题

- 为什么加载参数前必须先创建同样结构的模型？
- `unsqueeze(0)` 改变了哪个维度？
- `argmax(dim=1)` 为什么能得到预测数字？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 13 课](13-save-trained-model.md)

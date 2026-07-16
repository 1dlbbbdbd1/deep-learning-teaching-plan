# PyTorch MNIST 14 加载模型并预测单张图片

> 核心概念：load_state_dict、unsqueeze、argmax

# 第 14 课：加载模型并预测单张图片

这一课真正要解决的是：

```text
保存好的参数文件，怎样重新装回模型，并用它预测一张新图片？
```

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

## 源码逐段讲解

### 1. 先确认模型文件存在

```python
if not model_path.exists():
    raise FileNotFoundError(...)
```

如果第 13 课没有运行，模型文件不存在，这一课就无法加载参数。

### 2. 取测试集中的一张图片

```python
image, label = test_data[SAMPLE_INDEX]
```

这里用的是测试集，不是训练集。

`image` 是图片 Tensor，`label` 是正确答案。

### 3. 创建同样结构的模型

```python
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 10),
)
```

加载参数前必须先有同样结构的模型。参数文件只保存数字，不保存你这段模型结构代码。

### 4. 加载参数

```python
state_dict = torch.load(model_path, map_location="cpu")
model.load_state_dict(state_dict)
```

第一行把参数文件读出来。

第二行把参数装进模型。

### 5. 给单张图片补 batch 维度

```python
single_image_batch = image.unsqueeze(0)
```

单张图片形状是 `[1, 28, 28]`。

模型习惯接收一批图片，所以要变成 `[1, 1, 28, 28]`。

最前面的 `1` 表示：这一批里只有一张图片。

### 6. 预测类别

```python
scores = model(single_image_batch)
prediction = scores.argmax(dim=1).item()
```

模型输出 10 个分数，`argmax` 取最高分的位置作为预测数字。

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

## 输出怎么读

- `图片 batch 形状：[1, 1, 28, 28]`：一批里只有 1 张灰度图。
- `模型输出形状：[1, 10]`：这一张图对应 10 个分数。
- `真实标签`：标准答案。
- `预测结果`：模型猜的答案。
- `是否预测正确`：这次猜测有没有答对。

## 你真正学到了什么

到这里，最小闭环完成：

```text
训练 -> 保存参数 -> 创建同结构模型 -> 加载参数 -> 预测单张图片
```

这就是很多深度学习项目的核心套路，只是以后模型和数据会更复杂。

## 你可以自己改一改

把：

```python
SAMPLE_INDEX = 0
```

改成：

```python
SAMPLE_INDEX = 1
```

再运行脚本，观察真实标签和预测结果是否变化。

## 本节检查问题

- 为什么加载参数前必须先创建同样结构的模型？
- `unsqueeze(0)` 改变了哪个维度？
- `argmax(dim=1)` 为什么能得到预测数字？
- 参数文件保存了模型结构，还是只保存了参数数字？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 13 课](13-save-trained-model.md)

# PyTorch MNIST 02 认识 MNIST 数据

> 核心概念：Dataset、Tensor、transform、shape、像素范围

# 第 2 课：认识 MNIST 数据

这一课不是让你“运行成功就完事”。这一课真正要解决的是：

```text
MNIST 数据到底是什么？
PyTorch 为什么要把图片变成 Tensor？
代码里的 datasets、transforms、image、label、shape 分别在干什么？
```

你学完这一课，不需要会训练模型，但要能用自己的话解释：

```text
一条 MNIST 数据 = 一张图片 + 一个标签
图片进入 PyTorch 后会变成 Tensor
Tensor 的 shape 告诉我们这张图片的结构
```

## 先把几个词翻译成人话

| 词 | 先这样理解 | 在本课里对应什么 |
| --- | --- | --- |
| MNIST | 一个手写数字图片数据集 | 很多张 0 到 9 的手写数字图片 |
| Dataset | 数据仓库 | `train_data` |
| 样本 | 仓库里的一条数据 | 一张图片和它的答案 |
| label | 标准答案 | 这张图写的是几 |
| Tensor | PyTorch 用来计算的数据格式 | 图片被转成的数字数组 |
| transform | 数据进入模型前的转换步骤 | `transforms.ToTensor()` |
| shape | Tensor 的形状说明 | `torch.Size([1, 28, 28])` |

这些词后面会反复出现。现在不要背定义，先把它们和代码里的变量对上。

## MNIST 一条数据长什么样

MNIST 里的一条数据包含两部分：

```text
image：一张手写数字图片
label：这张图片的正确答案
```

比如第一条数据可能是：

```text
image：一张手写的 5
label：5
```

程序训练模型时，会让模型看 `image`，然后猜它是几。模型猜完之后，再拿 `label` 对答案。

## 为什么图片会变成 Tensor

电脑不能直接理解“这是一张手写的 5”。它只能处理数字。

所以图片会被转换成很多数字。每个数字表示一个像素有多亮：

```text
0.0 表示黑
1.0 表示白
中间的小数表示灰色
```

PyTorch 把这些数字放进 Tensor 里。你现在可以把 Tensor 理解成：

```text
专门给 PyTorch 用的多维数字表格
```

## `torch.Size([1, 28, 28])` 怎么读

MNIST 图片会变成这个形状：

```text
torch.Size([1, 28, 28])
```

它不是神秘符号，三个数字分别是：

- `1`：颜色通道数量。MNIST 是灰度图，只有黑白深浅，所以是 1。
- `28`：图片高度，28 个像素。
- `28`：图片宽度，28 个像素。

如果是彩色图片，通道通常会是 3，因为有红、绿、蓝三个颜色通道。

## 源码逐段讲解

本课脚本是：

```text
mnist_project/02_inspect_mnist_data.py
```

下面按代码顺序讲。

### 1. 导入工具

```python
from pathlib import Path

from torchvision import datasets, transforms
```

`Path` 用来处理文件夹路径。它比手写字符串路径更稳。

`torchvision` 是 PyTorch 生态里专门处理图片、常见数据集和图片转换的工具包。

`datasets` 里面有 MNIST 这种常用数据集。

`transforms` 里面有图片转换工具，比如把图片变成 Tensor。

### 2. 找到项目根目录和数据目录

```python
project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"
```

`__file__` 表示当前这个脚本文件的位置。

`resolve()` 会得到它的完整路径。

`parents[1]` 表示往上走两层，找到项目根目录。

`project_root / "data"` 表示在项目根目录下创建或使用 `data` 文件夹。

这几行的目的很简单：

```text
不管你从哪里运行脚本，数据都统一放到项目里的 data 目录。
```

### 3. 准备图片转换规则

```python
to_tensor = transforms.ToTensor()
```

MNIST 原始图片不是 Tensor。`ToTensor()` 会做两件事：

1. 把图片转成 PyTorch Tensor。
2. 把像素值缩放到 `0.0` 到 `1.0`。

如果没有这一步，后面很多 PyTorch 计算就不方便做。

### 4. 加载训练集

```python
train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=to_tensor,
)
```

这一段是在创建一个 MNIST 训练集对象。

每个参数的意思：

| 参数 | 意思 |
| --- | --- |
| `root=data_dir` | 数据保存在哪里 |
| `train=True` | 加载训练集，不是测试集 |
| `download=True` | 如果本地没有数据，就自动下载 |
| `transform=to_tensor` | 取出图片时，把图片转成 Tensor |

你可以把 `train_data` 理解成：

```text
一个装着 60000 条训练样本的数据仓库
```

### 5. 取出第一条样本

```python
image, label = train_data[0]
```

`train_data[0]` 表示取出第 0 条数据，也就是第一条数据。

它会返回两个东西：

```text
image：图片 Tensor
label：这张图片的答案
```

左边写成 `image, label`，意思是把这两个东西分别放进两个变量。

### 6. 打印我们要观察的东西

```python
print(f"训练集样本数：{len(train_data)}")
print(f"第一张图片的标签：{label}")
print(f"图片张量形状：{image.shape}")
print(f"图片张量最小值：{image.min().item():.1f}")
print(f"图片张量最大值：{image.max().item():.1f}")
```

这些输出不是装饰，它们分别回答问题：

| 输出 | 回答的问题 |
| --- | --- |
| `len(train_data)` | 训练集里有多少张图片 |
| `label` | 第一张图片的正确答案是什么 |
| `image.shape` | 图片 Tensor 的结构是什么 |
| `image.min()` | 图片里最暗的像素是多少 |
| `image.max()` | 图片里最亮的像素是多少 |

`.item()` 的作用是把只有一个数字的 Tensor 变成普通 Python 数字，方便打印。

`:.1f` 表示保留 1 位小数。

### 7. 自动检查结果是否合理

```python
if image.shape != (1, 28, 28):
    raise RuntimeError("MNIST 图片形状不符合预期。")

if not 0 <= label <= 9:
    raise RuntimeError("MNIST 标签不符合预期。")
```

这不是训练模型，只是在做基本检查：

- MNIST 图片应该是 `[1, 28, 28]`。
- MNIST 标签应该是 `0` 到 `9`。

如果不符合，脚本会主动报错，说明数据不正常。

### 8. 最后一行表示检查完成

```python
print("MNIST 数据验证通过")
```

这句话的意思不是“你完全学会了 MNIST”，而是：

```text
脚本确认了 MNIST 数据能加载，图片 shape 正常，标签范围正常。
```

## 运行脚本

```powershell
python .\mnist_project\02_inspect_mnist_data.py
```

第一次运行会下载 MNIST 到项目里的 `data/` 目录。这个目录已经写进 `.gitignore`，以后不会被 Git 收进去。

如果你看到类似输出：

```text
训练集样本数：60000
第一张图片的标签：5
图片张量形状：torch.Size([1, 28, 28])
图片张量最小值：0.0
图片张量最大值：1.0
MNIST 数据验证通过
```

## 输出怎么读

你要读懂的是：

- 训练集有 60000 张图片。
- 第一张图的标准答案是 5。
- 图片已经变成 Tensor。
- 图片结构是 1 个通道、28 高、28 宽。
- 像素已经被转换到 0.0 到 1.0。

## 你真正学到了什么

不是“脚本能运行”。真正学到的是：

1. MNIST 数据由图片和标签组成。
2. PyTorch 用 Tensor 表示图片。
3. `ToTensor()` 会把图片转成 Tensor，并缩放像素范围。
4. `shape` 是看懂深度学习代码的第一把钥匙。
5. 运行脚本时，要读输出背后的含义，而不是只看最后一句通过。

## 你可以自己改一改

试着把这行：

```python
image, label = train_data[0]
```

改成：

```python
image, label = train_data[1]
```

再运行脚本，观察：

- 标签会不会变？
- shape 会不会变？
- 最小值和最大值会不会仍然在 0.0 到 1.0？

如果 shape 不变，说明 MNIST 每张图片的结构都一样。标签变了，说明不同图片对应不同答案。

## 本节检查问题

请不要背答案，尽量用自己的话说：

- `Dataset` 在这一课里是什么？
- `image` 和 `label` 分别表示什么？
- `transforms.ToTensor()` 做了哪两件事？
- `torch.Size([1, 28, 28])` 里的三个数字分别表示什么？
- 为什么标签只可能是 `0` 到 `9`？
- 最后一行 `MNIST 数据验证通过` 到底验证了什么？

## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 1.5 课](01a-pytorch-common-map.md)
- 下一课：[第 3 课](03-mnist-visualization.md)

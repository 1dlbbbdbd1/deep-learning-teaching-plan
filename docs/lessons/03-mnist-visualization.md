# PyTorch MNIST 03 保存并查看手写数字图片

> 核心概念：PIL、灰度图、outputs 目录

# 第 3 课：把 MNIST 图片保存出来看一眼

这一课真正要解决的是：

```text
上一课只看到 Tensor 数字，这一课要确认这些数字真的对应一张手写数字图片。
```

## 今天只理解两个词

1. **PIL 图片**：Python 里常见的一种图片对象，可以直接保存成 `.png`。
2. **可视化**：把数据变成你能看的东西。对新手来说，这比盯着一堆数字更踏实。

上一课我们看到第一张图片的张量形状是：

```text
torch.Size([1, 28, 28])
```

这一课先不训练模型，只把第一张图片保存出来。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| PIL 图片 | Python 里能保存、打开、查看的图片对象 | `image.save(...)` |
| 灰度图 | 只有黑白深浅，没有彩色 | `image.mode` 输出 `L` |
| outputs 目录 | 专门放脚本生成结果的文件夹 | `output_dir` |
| label | 图片的标准答案 | 文件名里的 `label_5` |

## 源码逐段讲解

### 1. 准备路径

```python
project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"
output_dir = project_root / "outputs"
output_dir.mkdir(exist_ok=True)
```

这几行是在找项目根目录，并准备两个文件夹：

- `data`：放 MNIST 数据。
- `outputs`：放脚本生成的图片。

`mkdir(exist_ok=True)` 的意思是：如果 `outputs` 不存在就创建；如果已经存在，也不要报错。

### 2. 加载 MNIST 原始图片

```python
train_data = datasets.MNIST(
    root=data_dir,
    train=True,
    download=False,
)
```

这里没有写 `transform=ToTensor()`，所以取出来的 `image` 还是 PIL 图片，不是 Tensor。

这正是本课想要的：我们要把它直接保存成 `.png` 文件给人看。

### 3. 取出第一张图并组成文件名

```python
image, label = train_data[0]
output_path = output_dir / f"mnist_sample_0_label_{label}.png"
```

`train_data[0]` 返回第一张图片和它的答案。

文件名里写 `label_{label}`，是为了你打开图片时能知道它的标准答案是什么。

### 4. 保存图片

```python
image.save(output_path)
```

这行就是把 PIL 图片保存到 `outputs` 目录。

保存后，你就能用普通看图软件打开它，而不是只盯着 Tensor 数字。

## 运行脚本

```powershell
python .\mnist_project\03_save_mnist_image.py
```

期待看到：

```text
第一张图片的标签：5
图片模式：L
图片尺寸：(28, 28)
保存图片：outputs\mnist_sample_0_label_5.png
MNIST 图片保存验证通过
```

然后打开：

```text
outputs\mnist_sample_0_label_5.png
```

你应该能看到一张很小的手写数字 `5`。

## 输出怎么读

- `第一张图片的标签：5`：标准答案是 5。
- `图片模式：L`：这是灰度图，不是彩色图。
- `图片尺寸：(28, 28)`：图片宽 28 像素、高 28 像素。
- `保存图片：...`：告诉你图片文件保存在哪里。

注意：上一课 Tensor 形状是 `[1, 28, 28]`，这里图片尺寸是 `(28, 28)`。多出来的 `1` 是灰度通道，不是图片宽高。

## 你真正学到了什么

这一课不是训练模型，而是建立直觉：

```text
MNIST 不是抽象数字，它真的是一张张 28x28 的手写数字图片。
```

以后模型训练不正常时，第一步经常就是把数据可视化，看它是不是你以为的样子。

## 你可以自己改一改

把：

```python
image, label = train_data[0]
```

改成：

```python
image, label = train_data[1]
```

再运行脚本，观察保存出来的图片和文件名里的 label 是否变化。

## 本节检查问题

- 为什么脚本保存出来的文件名里带着 `label_5`？
- `图片尺寸：(28, 28)` 和上一课的 `torch.Size([1, 28, 28])` 有什么关系？
- 为什么这一课故意不使用 `transforms.ToTensor()`？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 2 课](02-mnist-data.md)
- 下一课：[第 4 课](04-dataloader-batches.md)

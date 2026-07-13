# PyTorch MNIST 01 PyTorch 安装验证

> 核心概念：PyTorch、CUDA、GPU 验证

# 第 1 课：安装并验证 PyTorch

## 今天只理解两个词

1. **torch**：PyTorch 的核心 Python 包。以后创建张量、写神经网络、训练模型，主要都从这里开始。
2. **CUDA**：NVIDIA 显卡用于加速计算的技术。你的电脑有 NVIDIA GPU，所以我们优先验证 GPU 能不能被 PyTorch 用上。

## 通用检查方式

```text
Python：请以本机实际版本为准
CUDA：请以本机实际版本和 PyTorch 官方选择器为准
GPU：CPU 或兼容的 NVIDIA GPU
```

请根据自己的系统访问 [PyTorch 官方安装页面](https://pytorch.org/get-started/locally/) 选择安装命令。不要直接复制其他电脑的驱动版本、CUDA 版本或绝对路径。

## 安装命令

确认终端前面是：

```text
(.venv) PS <project-root>>
```

然后运行：

```powershell
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

如果不确定当前 `python` 是谁，先运行：

```powershell
python .\mnist_project\00_check_environment.py
```

看到 `环境隔离验证通过` 再安装。

## 安装后验证

安装后会创建并运行：

```text
mnist_project/01_check_pytorch.py
```

期待看到：

```text
CUDA 是否可用：True 或 False
GPU 名称：以本机实际设备为准
PyTorch 验证通过
```

## 本节检查问题

- 为什么安装前要先确认终端在 `(.venv)`？
- `torch.cuda.is_available()` 如果是 `True`，说明了什么？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 上一课：[第 0 课](00-conda-isolation.md)
- 下一课：[第 2 课](02-mnist-data.md)

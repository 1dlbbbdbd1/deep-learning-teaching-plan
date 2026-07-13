# PyTorch MNIST 00 Conda 环境隔离

> 核心概念：隔离环境、解释器路径、sys.executable

# 第 0 课：先确认 Python 跑在哪个环境里

## 今天只理解两个词

1. **解释器**：真正执行 `.py` 文件的程序，也就是某个 `python.exe`。
2. **环境**：一个解释器，加上它能使用的一组包。

本项目要使用这个解释器：

```text
<project-root>\.venv\Scripts\python.exe
```

它属于 `.venv` 环境。以后我们安装 PyTorch、下载 MNIST、保存模型，都围绕这个环境做，不去污染 Anaconda 自带的 `base`。

## 第一个探针程序

文件：

```text
mnist_project/00_check_environment.py
```

现在先写最小版本：

```python
import sys

print(sys.executable)
```

这段代码的意思是：

- `import sys`：拿到 Python 自带的系统信息工具箱。
- `sys.executable`：当前正在运行代码的那个 `python.exe` 的完整路径。
- `print(...)`：把结果显示出来。

## VS Code 里最容易踩的坑

如果输出类似下面这样：

```text
<other-python>...
```

说明程序没有用到 `.venv`，而是跑到了 Windows 商店版 Python。

截图里出现了这种命令：

```text
python -u "<project-root>\mnist_project\00_check_environment.py"
```

这通常是 VS Code 的 Code Runner 插件在运行。它未必使用 VS Code 左下角或解释器列表里选中的 Python。

## 本节推荐运行方式

先打开 VS Code 下方面板里的“终端”，运行：

```powershell
& ".\.venv\Scripts\python.exe" ".\mnist_project\00_check_environment.py"
```

看到下面这个路径，就说明环境对了：

```text
<project-root>\.venv\Scripts\python.exe
```

## 这不是 Bash，是 PowerShell

如果终端前面长这样：

```text
PS <project-root>
```

这里有三层意思：

- `PS`：当前终端是 PowerShell，不是 Bash。
- `<project-root>`：当前所在的项目目录。

刚才这条命令是在项目目录的 PowerShell 终端中输入的：

```powershell
& ".\.venv\Scripts\python.exe" ".\mnist_project\00_check_environment.py"
```

但它用的是完整路径，所以仍然会调用 `.venv` 里的解释器。

下一步可以把环境切过去，让命令变短：

```powershell
.\.venv\Scripts\Activate.ps1
python .\mnist_project\00_check_environment.py
```

这时提示符应该包含 `(.venv)`，输出仍然应该是：

```text
<project-root>\.venv\Scripts\python.exe
```

## 本节检查问题

- 你看到的输出路径是 `.venv` 里的 Python，还是系统中其他 Python？
- 为什么“打印解释器路径”可以证明当前项目跑在哪个环境里？


## 相关链接

- 索引：[课程索引](../course-index.md)
- 总览：[项目总览](../project-overview.md)
- 下一课：[第 1 课](01-pytorch-installation.md)

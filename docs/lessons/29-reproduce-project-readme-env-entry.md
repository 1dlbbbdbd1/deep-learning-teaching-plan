# PyTorch MNIST 29 复刻项目前先读 README、环境和入口

> 核心概念：README、依赖、入口文件

# 第 29 课：复刻项目不是先改代码

复刻项目第一步是搞清楚它怎么运行，而不是凭感觉开改。

先确认三件事：

```text
README 说怎么跑
依赖怎么装
入口文件在哪里
```

## README 要读什么

重点找：

- 环境要求。
- 安装命令。
- 数据准备。
- 训练命令。
- 评估命令。
- 输出位置。

## 入口文件是什么

入口文件通常是 `train.py`、`main.py`、`predict.py` 或某个 notebook。入口文件告诉你项目从哪里开始执行。

## 实操清单

## 运行脚本

```powershell
python .\mnist_project\29_reproduce_project_entry_checklist.py
```

看到 `复刻项目入口检查验证通过`，说明你已经知道复刻前要先检查哪些入口。

- 给一个项目写运行路线图。
- 标出训练入口和评估入口。
- 不改代码，先跑原命令。
- 记录第一条报错。

## 先把术语翻译成人话

| 词 | 人话解释 | 本课里在哪里出现 |
| --- | --- | --- |
| README | 项目的说明书 | `README.md` |
| entry point | 程序从哪里开始跑 | `train.py`、`main.py` 等 |
| dependency | 项目依赖的软件包 | `requirements.txt`、安装命令 |
| checklist | 复刻前检查清单 | `required_entries` |

## 源码逐段讲解

### 1. 找到项目根目录

```python
project_root = Path(__file__).resolve().parents[1]
```

这行的意思是：从当前脚本位置往上找一级，得到项目根目录。

以后不要把本机绝对路径写死在脚本里。项目路径应该尽量从当前文件推出来。

### 2. 列出必须存在的入口

```python
required_entries = [
    project_root / "README.md",
    project_root / "docs" / "course-index.md",
    project_root / "mnist_project",
    project_root / "tests",
]
```

这份清单不是“训练模型”，而是“复刻前先确认项目骨架完整”。

### 3. 逐个检查

```python
for entry in required_entries:
    print(f"检查入口：{entry.relative_to(project_root)} -> {entry.exists()}")
```

`entry.exists()` 会返回 `True` 或 `False`。

`relative_to(project_root)` 让输出更干净，不暴露你的本机绝对路径。

### 4. 缺东西就立刻停

```python
if not entry.exists():
    raise RuntimeError(...)
```

复刻项目时，缺 README、缺源码目录、缺测试目录，都不应该继续硬猜。

## 输出怎么读

- `检查入口：README.md -> True`：README 存在。
- `检查入口：docs/course-index.md -> True`：课程索引存在。
- `检查入口：mnist_project -> True`：源码目录存在。
- `检查入口：tests -> True`：测试目录存在。

如果某一项是 `False`，先补齐或确认项目结构，而不是继续乱跑命令。

## 你真正学到了什么

复刻项目第一步不是写代码，而是建立项目地图：

```text
说明书在哪里？
依赖怎么装？
训练从哪里进？
评估从哪里进？
测试怎么跑？
```

没有地图就开始改代码，很容易把问题越改越大。

## 你可以自己改一改

把清单里临时加一项：

```python
project_root / "not_exist.py"
```

再运行脚本。它会报错，告诉你缺少入口。

这个实验想让你练习：让脚本帮你发现项目结构问题，而不是靠眼睛猜。

## Debug 检查

如果第一步就报错，先判断是环境问题、路径问题、依赖问题，还是数据缺失。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 28 课](28-train-evaluate-cnn.md)
- 下一课：[第 30 课](30-reproduce-data-pipeline.md)

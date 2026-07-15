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

## Debug 检查

如果第一步就报错，先判断是环境问题、路径问题、依赖问题，还是数据缺失。

## 相关链接

- 索引：[课程索引](../course-index.md)
- 上一课：[第 28 课](28-train-evaluate-cnn.md)
- 下一课：[第 30 课](30-reproduce-data-pipeline.md)

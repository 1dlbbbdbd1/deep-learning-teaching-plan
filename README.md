# PyTorch 深度学习循序学习计划

一个面向零基础学习者的公开学习仓库：从 MNIST 手写数字识别开始，逐步理解 PyTorch 的数据、模型、损失、梯度、训练、评估、保存和预测。

目标不是一次看完大而全的教程，而是每次只学习一个小概念，运行一段代码，观察一个结果，再记录自己的理解和问题。

## 当前进度

- MNIST 线性模型闭环：已完成
- 课程：第 00–14 课已完成
- 测试集准确率：当前学习记录为 88.62%
- 下一阶段：机器学习基础、MLP、CNN、项目复刻与 Debug

详细进度见 [`docs/progress.md`](docs/progress.md)。

## 快速开始

### 1. 获取代码并创建独立环境

```powershell
git clone https://github.com/1dlbbbdbd1/deep-learning-teaching-plan.git
cd deep-learning-teaching-plan
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install torch torchvision
```

如果需要使用 GPU，请根据自己的系统和显卡，选择 [PyTorch 官方安装方式](https://pytorch.org/get-started/locally/)，不要直接照抄其他人的本机命令。

### 2. 按课程顺序学习

从 [`docs/course-index.md`](docs/course-index.md) 开始。每一课都对应一个 `mnist_project/` 下的可运行脚本。

### 3. 下载并检查 MNIST

```powershell
python .\mnist_project\02_inspect_mnist_data.py
```

数据会下载到本地 `data/` 目录；该目录不会提交到 GitHub。

### 4. 运行测试

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

部分测试需要先下载 MNIST 数据，完整训练测试也可能需要较长时间。

## 仓库结构

```text
docs/
  course-index.md                 # 课程索引
  project-overview.md             # MNIST 项目总览
  progress.md                     # 公共学习进度
  lessons/                        # 第 00–14 课
  roadmap/                        # 十周深度学习路线
  debugging/                      # Debug 工作流与记录模板
mnist_project/                    # 逐课可运行代码
tests/                            # 自动验证
.github/                          # 提问、报错和协作模板
```

## 学习约定

1. 每次只引入 1–2 个新概念。
2. 先运行和观察，再解释抽象概念。
3. 代码、数据和模型都使用仓库相对路径。
4. 遇到报错时记录现象、最小复现、证据、根因和回归验证。
5. 分享日志前删除本机路径、用户名、密钥和其他隐私。

## 参与学习

- 不理解某一课：使用 [问题反馈模板](.github/ISSUE_TEMPLATE/question.yml)。
- 发现代码或文档问题：使用 [Bug 模板](.github/ISSUE_TEMPLATE/bug-report.yml)。
- 想补充示例或改进解释：先阅读 [`CONTRIBUTING.md`](.github/CONTRIBUTING.md)。

欢迎把自己的运行结果和理解写成清晰、可复现、已脱敏的反馈。

# Obsidian 课程同步约定

本仓库和 Obsidian 是两个互相配合、彼此独立的目录：

- GitHub 工作目录：`pytorch/`，保存可公开的教程、源码和测试。
- Obsidian 学习目录：`deep-learning/`，保存本地课程笔记和个人学习记录。

## 低影响原则

1. 不移动、删除或重命名 Obsidian 学习目录中的课程笔记。
2. 不修改 `.obsidian/` 配置，不把 Obsidian 配置同步到 GitHub。
3. 不把本机绝对路径、用户名、本地环境名称、硬件信息、数据集、模型权重或个人学习记录提交到远端。
4. Obsidian 中的 `[[双向链接]]` 只保留在本地笔记；公开副本使用仓库相对 Markdown 链接。
5. `欢迎.md` 等 Obsidian 初始化文件不纳入公开课程。

## 后续新增课程流程

以后新增教程时，按下面顺序处理：

1. 在 `docs/lessons/` 写好公开版教程。除过渡阅读课外，在 `mnist_project/` 添加对应示例脚本，在 `tests/` 添加最小验证。
2. 在 `docs/course-index.md`、`docs/progress.md` 和需要的项目总览中补上入口。
3. 完成敏感信息检查，把公开版教程复制一份到 Obsidian 的 `deep-learning/` 目录。
4. Obsidian 副本可以继续添加个人理解、运行结果和 `[[双向链接]]`；这些内容默认不回写到公开版。
5. 运行测试和链接检查，再提交 GitHub。

## 文件命名对应

公开课程使用便于 GitHub 浏览的英文文件名，例如：

```text
docs/lessons/15-features-labels-train-test.md
```

Obsidian 使用带课程编号的中文标题，例如：

```text
PyTorch MNIST 15 特征、标签、训练集和测试集.md
```

两份文件内容保持课程主线一致，但 Obsidian 版本允许包含个人学习记录。

## 推送前检查

```powershell
rg -n -i "[A-Za-z]:\\\\|/Users/|/home/|api[_-]?key|secret|token" docs mnist_project tests README.md
python -m unittest discover -s tests -p "test_*.py" -v
```

检查通过后，使用仓库实际 Git 元数据提交：

```powershell
git --git-dir=.git-public --work-tree=. status
git --git-dir=.git-public --work-tree=. add README.md docs mnist_project tests learning-progress.json
git --git-dir=.git-public --work-tree=. commit -m "sync latest lessons and learning progress"
git --git-dir=.git-public --work-tree=. push origin main
```

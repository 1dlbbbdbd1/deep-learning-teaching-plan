# PyTorch MNIST 项目总览

## 项目目标

从零基础出发，用 PyTorch 完成一个最小版 MNIST 手写数字识别程序：准备独立环境、安装并验证 PyTorch、加载 MNIST、搭建线性模型、训练、评估、保存模型，再重新加载模型预测单张图片。

## 当前结果

- 独立 Python 环境：由学习者在本地创建
- PyTorch：以本地安装的兼容版本为准
- 设备：CPU 或兼容的 CUDA GPU 均可
- 当前学习记录的测试集准确率：88.62%
- 训练、评估、保存、加载和预测闭环：已完成

## 学习路线

1. 先确认代码由哪个 Python 解释器执行。
2. 再验证 PyTorch、CUDA 和设备是否可用。
3. 逐层理解 MNIST 数据、batch、模型输出、loss、梯度和优化器。
4. 从一次训练步骤扩展到小循环，再扩展到完整 epoch。
5. 用测试集准确率判断模型是否真的学到东西。
6. 保存并加载模型，完成最小识别闭环。

## 后续学习计划

MNIST 闭环完成后，进入 [`roadmap/deep-learning-plan.md`](roadmap/deep-learning-plan.md)，先补齐机器学习和深度学习基础，再练习 MLP、CNN、项目复刻和 Debug，最后拆解最小 ViT。

当前已写入第 15–18 课，主题是特征、标签、训练集、测试集、线性回归、逻辑回归、决策树和随机森林。每课都配有一个最小可运行脚本，其中第 16–17 课包含玩具训练过程。

## 相关入口

- [课程索引](course-index.md)
- [第 14 课：加载模型并预测](lessons/14-load-model-and-predict.md)
- [第 15 课：特征、标签、训练集和测试集](lessons/15-features-labels-train-test.md)
- [第 16 课：线性回归](lessons/16-linear-regression.md)
- [第 17 课：逻辑回归](lessons/17-logistic-regression.md)
- [第 18 课：决策树和随机森林](lessons/18-decision-tree-random-forest.md)
- [学习进度](progress.md)
- [Debug 工作流](debugging/debug-workflow.md)

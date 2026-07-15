# PyTorch MNIST 课程索引

这是一个从环境到最小识别闭环的渐进式课程。建议按照顺序学习，每课先阅读说明，再运行对应脚本，最后回答课末问题。

## 课程列表

| 课程 | 主题 | 代码 |
| --- | --- | --- |
| 00 | [独立环境与解释器](lessons/00-conda-isolation.md) | [`00_check_environment.py`](../mnist_project/00_check_environment.py) |
| 01 | [PyTorch 安装验证](lessons/01-pytorch-installation.md) | [`01_check_pytorch.py`](../mnist_project/01_check_pytorch.py) |
| 01.5 | [PyTorch 常用功能速览](lessons/01a-pytorch-common-map.md) | 过渡阅读课，无需脚本 |
| 02 | [认识 MNIST 数据](lessons/02-mnist-data.md) | [`02_inspect_mnist_data.py`](../mnist_project/02_inspect_mnist_data.py) |
| 03 | [保存并查看手写数字图片](lessons/03-mnist-visualization.md) | [`03_save_mnist_image.py`](../mnist_project/03_save_mnist_image.py) |
| 04 | [DataLoader 和 Batch](lessons/04-dataloader-batches.md) | [`04_inspect_dataloader_batch.py`](../mnist_project/04_inspect_dataloader_batch.py) |
| 05 | [最小模型前向传播](lessons/05-minimal-model-forward.md) | [`05_minimal_model_forward.py`](../mnist_project/05_minimal_model_forward.py) |
| 06 | [交叉熵损失](lessons/06-loss-function.md) | [`06_compute_loss.py`](../mnist_project/06_compute_loss.py) |
| 07 | [反向传播](lessons/07-backpropagation.md) | [`07_backpropagation.py`](../mnist_project/07_backpropagation.py) |
| 08 | [优化器更新参数](lessons/08-optimizer-step.md) | [`08_optimizer_step.py`](../mnist_project/08_optimizer_step.py) |
| 09 | [一次完整训练步骤](lessons/09-one-batch-training-step.md) | [`09_one_batch_training_step.py`](../mnist_project/09_one_batch_training_step.py) |
| 10 | [小训练循环](lessons/10-mini-training-loop.md) | [`10_mini_training_loop.py`](../mnist_project/10_mini_training_loop.py) |
| 11 | [完整 Epoch 训练](lessons/11-one-epoch-training.md) | [`11_one_epoch_training.py`](../mnist_project/11_one_epoch_training.py) |
| 12 | [测试集准确率](lessons/12-evaluate-test-set.md) | [`12_evaluate_test_set.py`](../mnist_project/12_evaluate_test_set.py) |
| 13 | [保存训练好的模型](lessons/13-save-trained-model.md) | [`13_save_trained_model.py`](../mnist_project/13_save_trained_model.py) |
| 14 | [加载模型并预测单张图片](lessons/14-load-model-and-predict.md) | [`14_load_model_and_predict.py`](../mnist_project/14_load_model_and_predict.py) |
| 15 | [特征、标签、训练集和测试集](lessons/15-features-labels-train-test.md) | [`15_features_labels_train_test.py`](../mnist_project/15_features_labels_train_test.py) |
| 16 | [线性回归](lessons/16-linear-regression.md) | [`16_train_linear_regression.py`](../mnist_project/16_train_linear_regression.py) |
| 17 | [逻辑回归](lessons/17-logistic-regression.md) | [`17_train_logistic_regression.py`](../mnist_project/17_train_logistic_regression.py) |
| 18 | [决策树和随机森林](lessons/18-decision-tree-random-forest.md) | [`18_decision_tree_random_forest.py`](../mnist_project/18_decision_tree_random_forest.py) |
| 19 | [Tensor 的 shape、dtype 和 device](lessons/19-tensor-shape-dtype-device.md) | [`19_inspect_tensor_metadata.py`](../mnist_project/19_inspect_tensor_metadata.py) |
| 20 | [Dataset、transform 和 normalization](lessons/20-dataset-transform-normalization.md) | [`20_dataset_transform_normalization.py`](../mnist_project/20_dataset_transform_normalization.py) |
| 21 | [自己写一个 nn.Module](lessons/21-custom-nn-module.md) | [`21_custom_nn_module.py`](../mnist_project/21_custom_nn_module.py) |
| 22 | [激活函数为什么有用](lessons/22-activation-functions.md) | [`22_activation_functions.py`](../mnist_project/22_activation_functions.py) |
| 23 | [MLP 前向传播](lessons/23-mlp-forward.md) | [`23_mlp_forward.py`](../mnist_project/23_mlp_forward.py) |
| 24 | [训练一个 MNIST MLP](lessons/24-train-mnist-mlp.md) | [`24_train_mnist_mlp_toy.py`](../mnist_project/24_train_mnist_mlp_toy.py) |
| 25 | [学习率、batch size、epoch 和过拟合](lessons/25-hyperparameters-overfitting.md) | [`25_hyperparameters_overfitting_demo.py`](../mnist_project/25_hyperparameters_overfitting_demo.py) |
| 26 | [卷积、卷积核和特征图](lessons/26-convolution-feature-map.md) | [`26_convolution_feature_map.py`](../mnist_project/26_convolution_feature_map.py) |
| 27 | [池化、通道和最小 CNN](lessons/27-pooling-channels-cnn.md) | [`27_pooling_channels_cnn.py`](../mnist_project/27_pooling_channels_cnn.py) |
| 28 | [训练和评估 MNIST CNN](lessons/28-train-evaluate-cnn.md) | [`28_train_evaluate_cnn_toy.py`](../mnist_project/28_train_evaluate_cnn_toy.py) |
| 29 | [复刻项目前先读 README、环境和入口](lessons/29-reproduce-project-readme-env-entry.md) | [`29_reproduce_project_entry_checklist.py`](../mnist_project/29_reproduce_project_entry_checklist.py) |
| 30 | [复刻数据流](lessons/30-reproduce-data-pipeline.md) | [`30_reproduce_data_pipeline.py`](../mnist_project/30_reproduce_data_pipeline.py) |
| 31 | [复刻模型、loss 和训练循环](lessons/31-reproduce-model-loss-training-loop.md) | [`31_reproduce_model_loss_training_loop.py`](../mnist_project/31_reproduce_model_loss_training_loop.py) |
| 32 | [Debug 工作流实战](lessons/32-debug-workflow-practice.md) | [`32_debug_workflow_practice.py`](../mnist_project/32_debug_workflow_practice.py) |
| 33 | [常见错误专项训练](lessons/33-common-bug-drills.md) | [`33_common_bug_drills.py`](../mnist_project/33_common_bug_drills.py) |
| 34 | [ViT 的 patch embedding](lessons/34-vit-patch-embedding.md) | [`34_vit_patch_embedding.py`](../mnist_project/34_vit_patch_embedding.py) |
| 35 | [ViT 的 Encoder 和分类头](lessons/35-vit-encoder-classifier.md) | [`35_vit_encoder_classifier.py`](../mnist_project/35_vit_encoder_classifier.py) |
| 36 | [最终复刻报告和 Debug 复盘](lessons/36-final-reproduction-report.md) | [`36_final_reproduction_report.py`](../mnist_project/36_final_reproduction_report.py) |

## 项目入口

- [项目总览](project-overview.md)
- [公开学习进度](progress.md)
- [十周深度学习路线](roadmap/deep-learning-plan.md)
- [完整课程大纲](roadmap/full-course-outline.md)
- [Debug 工作流](debugging/debug-workflow.md)
- [Obsidian 同步约定](obsidian-sync.md)

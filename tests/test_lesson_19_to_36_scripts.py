from pathlib import Path
import os
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)


LESSON_SCRIPTS = [
    ("19_inspect_tensor_metadata.py", "Tensor 元数据验证通过"),
    ("20_dataset_transform_normalization.py", "Dataset transform normalization 验证通过"),
    ("21_custom_nn_module.py", "自定义 nn.Module 验证通过"),
    ("22_activation_functions.py", "激活函数验证通过"),
    ("23_mlp_forward.py", "MLP 前向传播验证通过"),
    ("24_train_mnist_mlp_toy.py", "MNIST MLP 玩具训练验证通过"),
    ("25_hyperparameters_overfitting_demo.py", "超参数和过拟合演示验证通过"),
    ("26_convolution_feature_map.py", "卷积和特征图验证通过"),
    ("27_pooling_channels_cnn.py", "池化和最小 CNN 验证通过"),
    ("28_train_evaluate_cnn_toy.py", "CNN 玩具训练评估验证通过"),
    ("29_reproduce_project_entry_checklist.py", "复刻项目入口检查验证通过"),
    ("30_reproduce_data_pipeline.py", "复刻数据流验证通过"),
    ("31_reproduce_model_loss_training_loop.py", "复刻训练闭环验证通过"),
    ("32_debug_workflow_practice.py", "Debug 工作流实战验证通过"),
    ("33_common_bug_drills.py", "常见错误专项训练验证通过"),
    ("34_vit_patch_embedding.py", "ViT patch embedding 验证通过"),
    ("35_vit_encoder_classifier.py", "ViT Encoder 和分类头验证通过"),
    ("36_final_reproduction_report.py", "最终复刻报告验证通过"),
]


class Lesson19To36ScriptTest(unittest.TestCase):
    def test_lesson_scripts_run_and_print_success_markers(self):
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"

        for script_name, success_marker in LESSON_SCRIPTS:
            with self.subTest(script=script_name):
                script = PROJECT_ROOT / "mnist_project" / script_name
                result = subprocess.run(
                    [str(PYTHON), str(script)],
                    cwd=PROJECT_ROOT,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    env=environment,
                    check=False,
                )

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(success_marker, result.stdout)


if __name__ == "__main__":
    unittest.main()

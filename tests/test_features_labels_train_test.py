from pathlib import Path
import os
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "15_features_labels_train_test.py"


class FeaturesLabelsTrainTestTest(unittest.TestCase):
    def test_script_explains_features_labels_and_split(self):
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"

        result = subprocess.run(
            [str(PYTHON), str(SCRIPT)],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=environment,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("特征矩阵形状：torch.Size([6, 2])", result.stdout)
        self.assertIn("标签形状：torch.Size([6])", result.stdout)
        self.assertIn("训练集样本数：4", result.stdout)
        self.assertIn("测试集样本数：2", result.stdout)
        self.assertIn("特征、标签、训练集和测试集验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import sys
import os
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "14_load_model_and_predict.py"
MODEL_PATH = PROJECT_ROOT / "models" / "mnist_linear_state_dict.pt"


class LoadModelAndPredictTest(unittest.TestCase):
    def test_saved_model_predicts_first_test_digit(self):
        if not MODEL_PATH.exists():
            subprocess.run(
                [str(PYTHON), str(PROJECT_ROOT / "mnist_project" / "13_save_trained_model.py")],
                cwd=PROJECT_ROOT,
                check=True,
            )

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
        self.assertIn("单张图片预测验证通过", result.stdout)
        self.assertIn("真实标签：7", result.stdout)
        self.assertIn("预测结果：7", result.stdout)
        self.assertIn("是否预测正确：True", result.stdout)


if __name__ == "__main__":
    unittest.main()

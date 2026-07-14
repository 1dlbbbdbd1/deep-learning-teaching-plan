from pathlib import Path
import os
import re
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "17_train_logistic_regression.py"


class TrainLogisticRegressionTest(unittest.TestCase):
    def test_script_trains_tiny_classifier(self):
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
        self.assertIn("类别数：2", result.stdout)
        self.assertIn("逻辑回归训练验证通过", result.stdout)

        initial_loss = re.search(r"初始 loss：([0-9.]+)", result.stdout)
        final_loss = re.search(r"最终 loss：([0-9.]+)", result.stdout)
        accuracy = re.search(r"训练集准确率：([0-9.]+)", result.stdout)

        self.assertIsNotNone(initial_loss)
        self.assertIsNotNone(final_loss)
        self.assertIsNotNone(accuracy)

        self.assertLess(float(final_loss.group(1)), float(initial_loss.group(1)))
        self.assertGreaterEqual(float(accuracy.group(1)), 0.95)


if __name__ == "__main__":
    unittest.main()

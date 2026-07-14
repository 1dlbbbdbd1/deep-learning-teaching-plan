from pathlib import Path
import os
import re
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "16_train_linear_regression.py"


class TrainLinearRegressionTest(unittest.TestCase):
    def test_script_trains_tiny_linear_regression(self):
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
        self.assertIn("训练目标：y = 2 * x + 1", result.stdout)
        self.assertIn("线性回归训练验证通过", result.stdout)

        initial_loss = re.search(r"初始 loss：([0-9.]+)", result.stdout)
        final_loss = re.search(r"最终 loss：([0-9.]+)", result.stdout)
        learned_weight = re.search(r"学到的权重 w：([0-9.\\-]+)", result.stdout)
        learned_bias = re.search(r"学到的偏置 b：([0-9.\\-]+)", result.stdout)

        self.assertIsNotNone(initial_loss)
        self.assertIsNotNone(final_loss)
        self.assertIsNotNone(learned_weight)
        self.assertIsNotNone(learned_bias)

        self.assertLess(float(final_loss.group(1)), float(initial_loss.group(1)))
        self.assertAlmostEqual(float(learned_weight.group(1)), 2.0, delta=0.2)
        self.assertAlmostEqual(float(learned_bias.group(1)), 1.0, delta=0.2)


if __name__ == "__main__":
    unittest.main()

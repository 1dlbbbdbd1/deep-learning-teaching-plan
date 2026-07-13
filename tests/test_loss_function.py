from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "06_compute_loss.py"


class LossFunctionTest(unittest.TestCase):
    def test_cross_entropy_loss_is_positive_scalar(self):
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
        self.assertIn("模型输出形状：torch.Size([32, 10])", result.stdout)
        self.assertIn("真实标签形状：torch.Size([32])", result.stdout)
        self.assertIn("loss 形状：torch.Size([])", result.stdout)
        self.assertIn("损失函数验证通过", result.stdout)

        match = re.search(r"loss 数值：([0-9.]+)", result.stdout)
        self.assertIsNotNone(match)
        self.assertGreater(float(match.group(1)), 0.0)


if __name__ == "__main__":
    unittest.main()

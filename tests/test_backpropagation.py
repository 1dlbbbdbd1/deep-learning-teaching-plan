from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "07_backpropagation.py"


class BackpropagationTest(unittest.TestCase):
    def test_backward_creates_gradients_for_model_parameters(self):
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
        self.assertIn("backward 前梯度：None", result.stdout)
        self.assertIn("权重梯度形状：torch.Size([10, 784])", result.stdout)
        self.assertIn("偏置梯度形状：torch.Size([10])", result.stdout)
        self.assertIn("反向传播验证通过", result.stdout)

        match = re.search(r"权重梯度范数：([0-9.]+)", result.stdout)
        self.assertIsNotNone(match)
        self.assertGreater(float(match.group(1)), 0.0)


if __name__ == "__main__":
    unittest.main()

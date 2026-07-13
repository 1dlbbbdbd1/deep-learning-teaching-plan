from pathlib import Path
import sys
import os
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "05_minimal_model_forward.py"


class MinimalModelForwardTest(unittest.TestCase):
    def test_model_maps_image_batch_to_ten_scores(self):
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
        self.assertIn("输入图片 batch 形状：torch.Size([32, 1, 28, 28])", result.stdout)
        self.assertIn("展平后 batch 形状：torch.Size([32, 784])", result.stdout)
        self.assertIn("模型输出形状：torch.Size([32, 10])", result.stdout)
        self.assertIn("最小模型前向传播验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import sys
import os
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "04_inspect_dataloader_batch.py"


class DataLoaderBatchTest(unittest.TestCase):
    def test_first_batch_has_expected_shapes(self):
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
        self.assertIn("图片 batch 形状：torch.Size([32, 1, 28, 28])", result.stdout)
        self.assertIn("标签 batch 形状：torch.Size([32])", result.stdout)
        self.assertIn("DataLoader batch 验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "11_one_epoch_training.py"


class OneEpochTrainingTest(unittest.TestCase):
    def test_one_epoch_trains_over_all_training_samples(self):
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
        self.assertIn("完整 epoch 训练验证通过", result.stdout)
        self.assertIn("训练样本数：60000", result.stdout)
        self.assertIn("epoch 数：1", result.stdout)

        batch_count = re.search(r"训练 batch 数：(\d+)", result.stdout)
        average_loss = re.search(r"epoch 平均 loss：([0-9.]+)", result.stdout)
        early_loss = re.search(r"前 20 个 batch 平均 loss：([0-9.]+)", result.stdout)
        late_loss = re.search(r"后 20 个 batch 平均 loss：([0-9.]+)", result.stdout)

        self.assertIsNotNone(batch_count)
        self.assertIsNotNone(average_loss)
        self.assertIsNotNone(early_loss)
        self.assertIsNotNone(late_loss)

        self.assertEqual(int(batch_count.group(1)), 235)
        self.assertLess(float(average_loss.group(1)), 1.0)
        self.assertGreater(float(early_loss.group(1)), float(late_loss.group(1)))


if __name__ == "__main__":
    unittest.main()

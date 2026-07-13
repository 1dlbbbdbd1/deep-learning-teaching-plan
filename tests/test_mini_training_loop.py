from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "10_mini_training_loop.py"


class MiniTrainingLoopTest(unittest.TestCase):
    def test_five_batch_training_loop_reduces_loss(self):
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
        self.assertIn("小训练循环验证通过", result.stdout)
        self.assertIn("训练 batch 数：5", result.stdout)

        losses = re.findall(r"第 (\d+) 步 loss：([0-9.]+)", result.stdout)
        self.assertEqual(len(losses), 5, result.stdout)

        first_step, first_loss = losses[0]
        last_step, last_loss = losses[-1]
        self.assertEqual(first_step, "1")
        self.assertEqual(last_step, "5")
        self.assertGreater(float(first_loss), float(last_loss))


if __name__ == "__main__":
    unittest.main()

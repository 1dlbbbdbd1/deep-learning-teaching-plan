from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "09_one_batch_training_step.py"


class OneBatchTrainingStepTest(unittest.TestCase):
    def test_one_training_step_reduces_loss_on_same_batch(self):
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
        self.assertIn("一次训练步骤验证通过", result.stdout)

        before_match = re.search(r"训练前 loss：([0-9.]+)", result.stdout)
        after_match = re.search(r"训练后 loss：([0-9.]+)", result.stdout)
        self.assertIsNotNone(before_match)
        self.assertIsNotNone(after_match)

        loss_before = float(before_match.group(1))
        loss_after = float(after_match.group(1))
        self.assertGreater(loss_before, loss_after)


if __name__ == "__main__":
    unittest.main()

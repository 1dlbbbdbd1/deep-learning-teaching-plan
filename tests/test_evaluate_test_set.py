from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "12_evaluate_test_set.py"


class EvaluateTestSetTest(unittest.TestCase):
    def test_trained_model_reaches_reasonable_test_accuracy(self):
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
        self.assertIn("测试集准确率验证通过", result.stdout)
        self.assertIn("测试样本数：10000", result.stdout)

        correct_match = re.search(r"预测正确数：(\d+)", result.stdout)
        accuracy_match = re.search(r"测试集准确率：([0-9.]+)%", result.stdout)

        self.assertIsNotNone(correct_match)
        self.assertIsNotNone(accuracy_match)

        correct_count = int(correct_match.group(1))
        accuracy = float(accuracy_match.group(1))
        self.assertGreaterEqual(correct_count, 8500)
        self.assertGreaterEqual(accuracy, 85.0)


if __name__ == "__main__":
    unittest.main()

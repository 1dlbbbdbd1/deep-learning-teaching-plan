from pathlib import Path
import sys
import os
import re
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "08_optimizer_step.py"


class OptimizerStepTest(unittest.TestCase):
    def test_optimizer_step_changes_model_parameters(self):
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
        self.assertIn("optimizer.step 前后权重是否变化：True", result.stdout)
        self.assertIn("参数更新验证通过", result.stdout)

        match = re.search(r"权重变化量：([0-9.]+)", result.stdout)
        self.assertIsNotNone(match)
        self.assertGreater(float(match.group(1)), 0.0)


if __name__ == "__main__":
    unittest.main()

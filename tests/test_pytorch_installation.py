from pathlib import Path
import sys
import os
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "01_check_pytorch.py"


class PyTorchInstallationTest(unittest.TestCase):
    def test_pytorch_imports_and_sees_cuda(self):
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
        self.assertIn("PyTorch 验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

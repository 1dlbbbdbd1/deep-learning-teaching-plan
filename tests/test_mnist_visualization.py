from pathlib import Path
import sys
import os
import subprocess
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "03_save_mnist_image.py"
OUTPUT_IMAGE = PROJECT_ROOT / "outputs" / "mnist_sample_0_label_5.png"


class MNISTVisualizationTest(unittest.TestCase):
    def test_saves_first_mnist_sample_as_png(self):
        if OUTPUT_IMAGE.exists():
            OUTPUT_IMAGE.unlink()

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
        self.assertTrue(OUTPUT_IMAGE.exists())
        self.assertGreater(OUTPUT_IMAGE.stat().st_size, 0)
        self.assertIn("保存图片：outputs\\mnist_sample_0_label_5.png", result.stdout)
        self.assertIn("MNIST 图片保存验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

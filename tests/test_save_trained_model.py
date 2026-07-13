from pathlib import Path
import sys
import os
import subprocess
import unittest

import torch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "13_save_trained_model.py"
MODEL_PATH = PROJECT_ROOT / "models" / "mnist_linear_state_dict.pt"


class SaveTrainedModelTest(unittest.TestCase):
    def test_trained_model_state_dict_is_saved(self):
        if MODEL_PATH.exists():
            MODEL_PATH.unlink()

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
        self.assertIn("模型保存验证通过", result.stdout)
        self.assertIn("保存路径：", result.stdout)
        self.assertTrue(MODEL_PATH.exists())
        self.assertGreater(MODEL_PATH.stat().st_size, 1000)

        state_dict = torch.load(MODEL_PATH, map_location="cpu")
        self.assertIn("1.weight", state_dict)
        self.assertIn("1.bias", state_dict)
        self.assertEqual(tuple(state_dict["1.weight"].shape), (10, 784))
        self.assertEqual(tuple(state_dict["1.bias"].shape), (10,))


if __name__ == "__main__":
    unittest.main()

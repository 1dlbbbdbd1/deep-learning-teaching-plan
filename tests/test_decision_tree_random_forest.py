from pathlib import Path
import os
import subprocess
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
SCRIPT = PROJECT_ROOT / "mnist_project" / "18_decision_tree_random_forest.py"


class DecisionTreeRandomForestTest(unittest.TestCase):
    def test_script_compares_tree_and_forest_votes(self):
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
        self.assertIn("单棵决策树预测：1", result.stdout)
        self.assertIn("随机森林投票结果：1", result.stdout)
        self.assertIn("投票明细：[1, 1, 0]", result.stdout)
        self.assertIn("决策树和随机森林验证通过", result.stdout)


if __name__ == "__main__":
    unittest.main()

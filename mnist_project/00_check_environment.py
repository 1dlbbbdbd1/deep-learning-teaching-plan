from pathlib import Path
import sys

actual_environment = Path(sys.prefix).resolve()
base_environment = Path(getattr(sys, "base_prefix", sys.prefix)).resolve()

print(f"Python 版本：{sys.version.split()[0]}")
print(f"解释器路径：{sys.executable}")
print(f"环境目录：{actual_environment}")

if actual_environment == base_environment:
    print("提示：当前使用的是基础 Python，建议创建并激活项目独立环境。")
else:
    print("独立环境已检测到。")

print("环境检查通过")

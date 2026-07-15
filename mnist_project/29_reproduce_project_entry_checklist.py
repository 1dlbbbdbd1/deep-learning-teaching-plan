from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
required_entries = [
    project_root / "README.md",
    project_root / "docs" / "course-index.md",
    project_root / "mnist_project",
    project_root / "tests",
]

for entry in required_entries:
    print(f"检查入口：{entry.relative_to(project_root)} -> {entry.exists()}")
    if not entry.exists():
        raise RuntimeError(f"缺少复刻入口：{entry}")

print("复刻前先确认：README、课程索引、源码目录、测试目录")
print("复刻项目入口检查验证通过")

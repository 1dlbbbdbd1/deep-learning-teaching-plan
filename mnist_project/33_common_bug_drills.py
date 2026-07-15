bug_drills = [
    ("路径错误", "确认 cwd 和文件是否存在"),
    ("shape 错误", "打印输入、输出和 Linear/Conv2d 期待的 shape"),
    ("dtype 错误", "确认图片是 float，分类标签是 long"),
    ("device 错误", "确认模型和数据都在 CPU 或都在 GPU"),
    ("梯度错误", "确认 zero_grad、backward、step 顺序"),
    ("模式错误", "训练用 train，评估用 eval 和 no_grad"),
]

for name, check in bug_drills:
    print(f"{name}：{check}")

if len(bug_drills) != 6:
    raise RuntimeError("常见错误清单数量不符合预期。")

required = {"路径错误", "shape 错误", "dtype 错误", "device 错误", "梯度错误", "模式错误"}
actual = {name for name, _ in bug_drills}

if actual != required:
    raise RuntimeError("常见错误清单内容不完整。")

print("常见错误专项训练验证通过")

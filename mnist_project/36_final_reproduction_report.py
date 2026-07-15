required_sections = [
    "项目目标",
    "运行环境",
    "数据流",
    "模型结构",
    "训练流程",
    "评估结果",
    "Debug 记录",
    "最终结论",
    "仍然不懂的问题",
]

report = {
    "项目目标": "复刻一个最小 CNN 或 ViT 分类项目",
    "运行环境": "记录 Python、PyTorch、CUDA、依赖安装方式",
    "数据流": "记录 Dataset、transform、DataLoader、batch shape",
    "模型结构": "记录输入、关键层、输出 logits shape",
    "训练流程": "记录 loss、optimizer、epoch、batch size",
    "评估结果": "记录 accuracy 或其他指标",
    "Debug 记录": "记录现象、复现、证据、根因、修复、回归验证",
    "最终结论": "说明复刻是否成功",
    "仍然不懂的问题": "保留下一轮学习问题",
}

for section in required_sections:
    print(f"{section}：{report[section]}")

missing = [section for section in required_sections if section not in report]

if missing:
    raise RuntimeError(f"复刻报告缺少章节：{missing}")

print("最终复刻报告验证通过")

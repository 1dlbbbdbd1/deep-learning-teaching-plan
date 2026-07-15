import torch
from torch import nn


workflow = ["复现问题", "缩小输入", "提出假设", "增加证据", "最小修复", "回归验证"]

bad_input = torch.randn(2, 3)
model = nn.Linear(4, 2)

try:
    model(bad_input)
except RuntimeError as error:
    evidence = {
        "现象": "Linear 输入特征数不匹配",
        "输入 shape": tuple(bad_input.shape),
        "模型期待 in_features": model.in_features,
        "错误片段": str(error).splitlines()[0],
    }
else:
    raise RuntimeError("这个脚本应该先复现一个 shape 错误。")

fixed_input = torch.randn(2, 4)
fixed_output = model(fixed_input)

print(f"Debug 流程：{' -> '.join(workflow)}")
print(f"证据：{evidence}")
print(f"修复后输出 shape：{fixed_output.shape}")

if fixed_output.shape != (2, 2):
    raise RuntimeError("修复后的输出 shape 不符合预期。")

print("Debug 工作流实战验证通过")

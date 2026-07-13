import torch


print(f"PyTorch 版本：{torch.__version__}")
print(f"CUDA 是否可用：{torch.cuda.is_available()}")
print(f"PyTorch 使用的 CUDA 版本：{torch.version.cuda}")

if torch.cuda.is_available():
    print(f"GPU 名称：{torch.cuda.get_device_name(0)}")
    x = torch.rand(2, 3, device="cuda")
else:
    print("未检测到 CUDA GPU，继续使用 CPU 验证。")
    x = torch.rand(2, 3)

print(f"随机张量设备：{x.device}")

print("PyTorch 验证通过")

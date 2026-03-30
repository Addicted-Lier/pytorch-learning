import torch

print("--- AI Lab Status ---")
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA (GPU) Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"Current GPU: {torch.cuda.get_device_name(0)}")
    # This part creates a small piece of data and sends it to the GPU
    tensor = torch.ones(3, 3).to("cuda")
    print("✅ Successfully moved a Tensor to the GPU!")
    print(f"Tensor is living on: {tensor.device}")
else:
    print("⚠️ GPU not detected by PyTorch yet.")
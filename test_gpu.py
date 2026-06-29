import torch_directml
import torch

# Check the available device
device = torch_directml.device()
print(f"Found device: {device}")

# Simple math operation on the GPU to verify functionality
x = torch.tensor([1.0, 2.0]).to(device)
print(f"Calculation test: {x * 2}")
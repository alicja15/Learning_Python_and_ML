import torch_directml
import torch

# Sprawdzenie urządzenia
device = torch_directml.device()
print(f"Znalezione urządzenie: {device}")

# Prosta operacja matematyczna na GPU
x = torch.tensor([1.0, 2.0]).to(device)
print(f"Test obliczeń: {x * 2}")
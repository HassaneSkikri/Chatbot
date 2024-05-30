import torch

# Check if GPU is available
if torch.cuda.is_available():
    print("CUDA is available. You can use the GPU.")
else:
    print("CUDA is not available. Using CPU.")

# Create a tensor
x = torch.rand(5, 3)
print("hello")
print(x)

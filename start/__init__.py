from __future__ import print_function
import torch

x = torch.empty(3, 5)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

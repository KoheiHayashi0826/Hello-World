import numpy as np
import torch 
import matplotlib.pyplot as plt
import torchvision
import math 
print("Hello-World")
a = torch.tensor([1, 2])
print(a)

x = np.linspace(0, 0.6, 100)

y_1 =  1 - 0.5*np.exp(-5*x)
y_2 =  1- 5*0.5*np.exp(-5*x)/(5+2*(1-np.exp(-5*x)))
plt.plot(x, y_1, label="Case1")
plt.plot(x, y_2, label="Case2")
plt.legend()
plt.show()
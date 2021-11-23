import numpy
import torch 
print(1 + 1)
import torchvision
#import fbm
from fbm import FBM

f = FBM(n=10, hurst=0.5)
f_sample = f.fbm()
print(f_sample)

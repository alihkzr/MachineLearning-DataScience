# 1
import numpy as np
a = np.linspace(1, 100, 100)
b = np.logspace(np.log10(1), np.log10(100), num=100)
aa = a[1:] / a[:99]
bb = b[1:] / b[:-1]
print(aa)
print("----------------------------------")
print(bb)

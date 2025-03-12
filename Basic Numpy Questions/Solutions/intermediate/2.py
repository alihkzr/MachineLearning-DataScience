# 2
import numpy as np
import random
n = random.randint(1,100)
k = random.randint(1,100)
x = np.random.randint(1,100,(n,k))
print(x)
y = np.random.randint(1,100,(1,k))
print(y)
y = y / (np.sum(y))
print(y)
print(np.sum(y))
print("--------------")
z = x * y
print(z)
print("--------------")
print(np.mean(z, axis=1))
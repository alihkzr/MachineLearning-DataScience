# 3
import numpy as np
np.random.seed(3)
x = np.random.uniform(0, 5, (50, 365))
x[x<0.5] = np.nan
y = np.nancumsum(x, axis=1)
y = np.argmax(y>=150, axis=1)
print(y)
print("-------------------------")
z = x[:, :360].reshape(50,12,30)
z = np.nansum(z, axis=2) 
z = np.argmax(z, axis=1) + 1
print(z)
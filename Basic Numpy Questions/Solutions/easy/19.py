# 19
# یک ماتریس صد در دو از اعداد منفی ده تا ده بسازید این ماتریس نماینگر صد نقطه در محور مختصات است حال برای هر نقطه فصله آن را تا مبدا مختصات محاسبه کنید 
# و سپس این نقاط را به ترتیب کمترین فاصله تا بیشترین فاصله مرتب کنید

import numpy as np
u = np.random.randint(-10, 10,(5,2))
print(u)
print("---------------")
v = np.power(u,2)
print(v)
print("---------------")
w = v.sum(axis=1)
print(w)
print("---------------")
w = np.sqrt(w)
print(w)
print("---------------")
w = np.sort(w)
print(w)

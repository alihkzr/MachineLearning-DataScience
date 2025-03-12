# 23
# پنج بردار سه عنصری مجزا تولید کنید و آنها را به یکدیگر بچسبانید تا یک تنسور یک در سه در پنج بسازید

import numpy as np
x1 = np.arange(0,3)
x2 = np.arange(3,6)
x3 = np.arange(6,9)
x4 = np.arange(9,12)
x5 = np.arange(12,15)
print(np.concatenate((x1,x2,x3,x4,x5)).reshape(5,3,1))
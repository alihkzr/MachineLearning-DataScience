# 16
# یک ماتریس پنج در پنج بسازید و سپس سطر اول و ستون سوم آن را چاپ کنید

import numpy as np
r = np.random.randint(0,30, (5,5))
print(r)
print(r[0,:])
print(r[:,2])
# 11
# دو بردار به طول برابر بسازید یک بردار جدید بوجود آورید که عنصر آیُم آن برابر با ماکسیمم عنصر آیَم از بردار اول و عنصر آیَم از بردار دوم باشد

import numpy as np
l = np.random.randint(0, 30,(1,5))
print(l)
m = np.random.randint(0, 30,(1,5))
print(m)
print(np.maximum(l,m))

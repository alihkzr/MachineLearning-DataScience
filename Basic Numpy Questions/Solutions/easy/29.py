# 29
# یک بردار تصادفی از اعداد بین صفر و یک بسازید و سپس حاصل جمع و حاصل ضرب همه آنها را چاپ کنید

import numpy as np
x = np.random.rand(3).round(2)
print(x)
print(x.sum())
print(x.prod())
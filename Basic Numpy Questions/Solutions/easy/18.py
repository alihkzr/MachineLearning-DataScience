# 18
# یک ماتریس پنج در پنج بسازید و سپس تمام عناصر بیشتر از پانزده را با منفی یک جایگزین کنید 

import numpy as np
t = np.random.randint(0,30, (5,5))
print(t)
t[t > 15] = -1
print(t)
# 17
# یک ماتریس پنج در پنج بسازید و سپس یک زیر ماتریس دو در دو از گوشه بالا چپ آن استخراج کنید 

import numpy as np
s = np.arange(0,25).reshape(5,5)
print(s)
print(s[0:2,0:2])
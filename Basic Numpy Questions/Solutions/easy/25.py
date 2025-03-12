# 25
# یک ماتریس ده در ده بسازید که هر عنصر حاصل ضرب شماره سطر و شماره ستون خود است مشابه جدول ضرب و سپس قطر اصلی آن را برابر با صفر قرار دهید

import numpy as np
# FIRST METHOD
# z = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (10, 10), dtype=int)
# print(z)
# print(np.fill_diagonal(z, 0))

# SECOND METHOD
print(np.arange(1, 11).reshape(-1, 1) * np.arange(1, 10).reshape(1, -1))

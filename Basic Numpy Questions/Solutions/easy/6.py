# 6
# یک ماتریس سه در چهار که با اعداد تصادفی بین منفی صد و صد پر شده است را بسازید و سپس میانگین هر ستون را محاسبه کرده و این مقدار را از آن ستون کسر کنید (پس از انجام این کار باید میانگین هر ستون صفر شود)

import numpy as np
f = np.random.randint(-100,100,(3,4))
print(f)
print(f.mean(axis=0).round())
f = (f - (f.mean(axis=0).round()))
print(f)
print(f.mean(axis=0).round())

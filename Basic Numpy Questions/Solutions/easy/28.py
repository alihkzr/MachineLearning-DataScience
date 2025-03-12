# 28
# یک ماتریس شش در شش با اعداد تصادفی بسازید و سپس آن را به صورت عمودی بشکنید تا به سه تا ماتریس شش در دو برسید

import numpy as np
x = np.random.randint(0,30,(6,6))
print(x)
print("---------------")
z = x.reshape(6,3,2).transpose([1,0,2])
print(z)
# 5
# یک ماتریس چهار در چهار بسازید که در تمام خانه های آن به جز قطر اصلی عدد صفر نوشته شده مقدار هر خانه در قطر اصلی باید برابر با عدد هفت باشد

import numpy as np
e = np.identity(4)
e[e == 1] = 7
print(e)

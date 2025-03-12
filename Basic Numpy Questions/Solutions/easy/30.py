# 30
# یک بردار شامل اعداد زیر بسازید این اعداد بیانگر بیانگر درجه زاویه هستند سپس آنها را به رادیان تبدیل کرده و سینوس و کسینوس هر کدام را چاپ کنید

import numpy as np
x = np.array([0,30,45,60,90])
x = np.radians(x)
print(x)
print(np.sin(x).round(2))
print(np.cos(x).round(2))

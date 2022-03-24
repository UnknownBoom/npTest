import numpy as np

x = 5.4
a = 12.3

r = (np.tan(a * x) ** 2 + np.log(x)) / np.power(np.e ** x, 1/4)
print(np.isclose(r, 0.497, atol=0.01))
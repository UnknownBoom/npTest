import matplotlib.pyplot as pl
import numpy as np

nw = 100
ns = 100

draws = np.random.randint(0, 2, size=(nw, ns))
st = np.where(draws > 0, 1, -1)
w = st.cumsum(1)

a = 25

hitsa = (np.abs(w) >= a).any(1)
argm = w[hitsa].argmax(1)
print(f"Count hits {a} {hitsa.sum()}")
print(f"Row hits inds {a} {argm}")
print(f"Row hits {a} in source {draws[hitsa]}")
print(f"Row hits {a} in cumsun {w[hitsa]}")

pl.plot(w)
pl.xlabel('count')
pl.ylabel('values')


pl.show()



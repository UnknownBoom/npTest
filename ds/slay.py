import numpy as np
import numpy.linalg as la

a = np.asarray([[2, -1, 1], [-1, 1, 2], [1, 2, -1]])
b = np.asarray([4, 0, -2])

r = la.solve(a, b)

print(r)
print(np.dot(a, r) == b)

a = np.asarray([[0, 2, -3], [1, -1, -1], [1, -2, 2]])
b = np.asarray([1, -1, -3])

r = la.solve(a, b)

print(r)
print(np.dot(a, r) == b)

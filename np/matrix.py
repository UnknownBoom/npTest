import numpy as np
import numpy.linalg as linalg

a = np.asarray([1, 2])[:, np.newaxis]
b = np.asarray([-1, 4, 2])[np.newaxis, :]
z = 3

r = np.vstack((b, np.matmul(a, b) + z))
print(r)
print('---------------------------------------------')
print()

a = np.asarray([[13, 5, 15], [4, -2, 3], [1, 1, 7]]).reshape(-1, 3)
b = np.asarray([[1, 5], [5, 3], [-2, 7]]).reshape(-1, 2)

print(a.max() * b.T)
print('---------------------------------------------')
print()

a = np.asarray([[1, 7, 2], [4, 3, 7], [-1, 2, -9]]).reshape(-1, 3)
b = np.asarray([[6, 0, -4], [-2, 4, 5], [5, 9, 1]]).reshape(-1, 3)

print(linalg.det(linalg.inv(a - b)))
print('---------------------------------------------')
print()

a = np.asarray([[0, -2], [6, -3], [-4, 7]]).reshape(-1, 2)
b = np.asarray([[3, 1, 2], [6, -3, 7]]).reshape(-1, 3)

print(np.max(-np.matmul(a, b)))
print('---------------------------------------------')
print()

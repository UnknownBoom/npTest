import numpy as np


def p(a):
    print("------------------------------")
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype)
    print("------------------------------")
    print()


# arr = np.asarray([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# p(arr)
#
#
# arr = arr.reshape(-1, 1)
# p(arr)
#
# arr = arr.flatten()
# p(arr)
#
# arr = np.asarray([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# p(arr)
#
#
# arr = arr.T
# p(arr)
#
#
# arr = np.arange(100).reshape(5, -1)
# p(arr)
#
# arr = arr[np.newaxis, :]
# p(arr)
#
# arr = arr[:, np.newaxis]
# p(arr)
#
# arr = np.arange(10)[:, np.newaxis]
# p(arr)
#
# arr = np.arange(10)[np.newaxis,: ,np.newaxis]
# p(arr)
#
# arr = np.zeros(shape=(3,3))
# p(arr)
#
# arr = np.ones_like(arr)
# p(arr)
#
# arr = np.eye(4)
# p(arr)
#
#
# arr = np.arange(1, 10,3)
# p(arr)
#
# arr = np.linspace(0, 10, 9)
# p(arr)

# arr = np.eye(3)
# p(arr)
#
# arr2 = np.arange(1, 10).reshape(arr.shape)
# p(arr2)
#
# p(arr2 * arr )
#
# argmax = arr2.argmax()
# p(argmax)
#
# index = np.unravel_index(argmax, arr2.shape)
# print(arr2[index])
#
# arr = np.arange(10)
# barr = np.logical_not(arr)
#
# arr = barr + arr
# p(arr)
#
# p(arr * np.linspace(0, 10, 10).reshape(arr.shape))

# arr = np.arange(10).reshape(-1,2)
#
# arr2 = np.arange(arr.shape[0])[:, np.newaxis]
#
# p(arr)
# p(arr2)
# p(arr + arr2)

# arr = np.arange(20).reshape(10, -1)
# p(arr)
#
# arr2 = np.arange(10)
# p(arr2)
#
# p(arr + arr2[:, np.newaxis])

# arr = np.arange(10).reshape(-1, 2).reshape(2, -1)
# p(arr)

arr = np.arange(24).reshape(2, 3, 4)
# p(arr)

p(arr[1])

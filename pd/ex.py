import pstats

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import pandas as pd


def pp(arr):
    print(arr)
    print("-----------------------")
    print()


# type: la, np, plt
# a = pd.Series([2, 4, 6, 8])
# b = pd.Series([1, 3, 5, 7])
#
# r = 0
#
# print(np.sum(a - b) ** 0.5)
# print(la.norm(a - b))
# print("----------------------------------------------")
# print()
#
# df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4), columns=list('efgh'), index=list('abcd'))
# abs_corr = df.corr().abs()
# print(abs_corr)
# print()
# print(np.sort(abs_corr,axis=0))
# print()
# print(np.sort(abs_corr, axis=0)[-2])
# print()


# df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4))
# print(df)
# print()
#
# apply = df.apply(lambda x: (x - x.mean()) / x.std())
# print(apply)
# print()
# apply = apply.apply(lambda x: (x.max() - x) / (x.max()-x.min()))
# print(apply)


# df1: pd.DataFrame = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                                   'weight': ['low', 'medium', 'high'] * 3,
#                                   'price': np.random.randint(0, 100, 9)})
#
# df2: pd.DataFrame = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
#                                   'ves': ['low', 'high'] * 3,
#                                   'price': np.random.randint(0, 100, 6)})
# merge = pd.merge(df1, df2, left_on=['fruit', 'weight'], right_on=['frukt', 'ves'], how='inner')
# pp(merge)

# df = pd.DataFrame(np.random.randint(1, 10, 16).reshape(4, 4), columns=list('abcd'))
#
# pp(pd.value_counts(df.values.flatten()))

# ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser2 = pd.Series(np.arange(26))
#
# pp(pd.concat((ser1, ser2), axis=1))

# ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser.name = "qwerty"
# pp(ser)

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# pp(ser1[~ser1.isin(ser2)])

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# concat = pd.concat([ser1[~ser1.isin(ser2)], ser2[~ser2.isin(ser1)]], axis=1).values.flatten()
# print(concat[~np.isnan(concat)])

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# pp(np.intersect1d(ser2, ser1))

# ser = pd.Series(np.random.normal(0,1,100))
# pp(ser)
# pp(np.percentile(ser, [0, 25, 50, 75, 100, 78]))
# ser.plot()
# plt.show()


# ser = pd.DataFrame(np.random.rand(100, 2) * 4.5, columns=['A', 'B']).cumsum()
# pp(ser)
# ser.plot(x='A', y='B')
# plt.show()

# ser = (pd.Series(np.random.randn(10000)))
# pp(ser)
# ser.hist()
# plt.show()

# ser = pd.DataFrame(np.random.rand(100, 2) * 4.5, columns=['A', 'B'])
# pp(ser)
# ser.hist()
# plt.show()
# print(ser.skew())

# ser = pd.Series(np.random.randn(10000))
#
# ser = 1000 + 1000 * ser
#
# pp(ser)
# ser.hist()
# plt.show()
# print(ser.skew())

# ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
# pp(pd.value_counts(ser))

# np.random.RandomState(100)
# ser = pd.Series(np.random.randint(1, 5, [12]))
# pp(ser)
# sort = pd.value_counts(ser)
# pp(sort)
# pp(ser.map(lambda x: x if x in sort.values[:2] else 'Other'))


ser = pd.Series(np.random.random(20))
pp(ser)
pp(pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
        labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']))
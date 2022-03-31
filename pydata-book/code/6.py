import numpy as np
import pandas as pd
def qwerty(x):
    print(x)
    print()

p = qwerty
# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b', 'd'],
#                    'data1': range(7)})
#
# print(df)
# print()
#
# print(pd.get_dummies(df['key'], prefix='key'))
mnames = ['movie_id', 'title', 'genres']
table = pd.read_table('../datasets/movielens/movies.dat', sep='::', header=None, names=mnames)
genres = []
table['genres'].map(lambda x: genres.extend(x.split('|')))
genres = pd.unique(genres)
p(genres)

zero = np.zeros((len(table), len(genres)))
p(zero)
dummies = pd.DataFrame(zero, columns=genres)
p(dummies)

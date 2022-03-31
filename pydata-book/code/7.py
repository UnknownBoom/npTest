import matplotlib.pyplot as pl
import numpy as np
import pandas as pd

# data = pd.read_csv('../examples/spx.csv', index_col=0, parse_dates=True)
#
# data.plot(ylabel='SPX')
# pl.xlim('2007', '2011')
# pl.show()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))
print(df)
print()
df.plot(subplots=True)
pl.show()

df.value_counts().plot.bar()
pl.show()

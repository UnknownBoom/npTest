import numpy as np
import pandas as pd

arange = np.arange(-10, 10)

bins = [-11, 0, 11]
cut: pd.Categorical = pd.cut(arange, bins)
print(cut )
print()


print(cut.value_counts())

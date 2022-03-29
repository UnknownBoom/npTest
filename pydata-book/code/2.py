import numpy as np
import pandas as pd

series = pd.DataFrame(np.arange(0, 12).reshape(-1, 3))
print(series)
apply = series.apply(lambda x: x.max(), axis=1)
print()
print(apply)
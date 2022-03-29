import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 5, 4, 5]})

print(data)
print()

res = data.apply(pd.value_counts).fillna(0)
print(res)
res.plot.bar()
data.hist()
plt.show()

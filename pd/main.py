import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)

# series = pd.Series({b: i for i, b in enumerate(string.ascii_lowercase, 1)})
# print(series)
# print(series[['a']])
# print(series[[0]])
# print("-------------------------------")
# print()
#

#
# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )
#
# print(df)
# print("-------------------------------")
# print()

# df = pd.read_csv('data.csv')
#
# level_1 = df[df.level > 0]
#
# level_1['description'] = level_1['description'].apply(lambda x: x[:25])
#
# level_1.tail(3).to_csv('data1.csv', encoding='UTF-8', index=False)
#
# level_0 = df[df.level == 0]
#
# level_0['description'] = level_0['description'].apply(lambda x: x[:25])
#
# level_0.tail(4).to_csv('data1.csv', header=False, encoding='UTF-8', index=False, mode='a')

df = pd.read_csv('data1.csv')
print(df.level > 0)
print(df[df.level > 0][['industry', 'size']])
print("--------------------------------------")
print()

df['ind_len'] = df['industry'].map(len)
print(df)
print("--------------------------------------")
print()

df.drop(['ind_len'], axis=1, inplace=True)
print(df)
print("--------------------------------------")
print()


print(df.describe())
print("--------------------------------------")
print()

print(df.level.value_counts())
print("--------------------------------------")
print()

print(df.info())
print("--------------------------------------")
print()

print(df.shape)
print("--------------------------------------")
print()


import pandas as pd

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
column_names = df.columns

print(column_names)
print(df.head())
print(df.tail())
print(df.shape)
print(df.count())

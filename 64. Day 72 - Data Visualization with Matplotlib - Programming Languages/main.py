import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
print(df.head())
print(df.tail())
print(df.shape)
print(df.count())
print(df.groupby('TAG').sum())
print(df.groupby('TAG').count())

# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)
print(df.head())

# Testing Start
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
                        'Power': [100, 80, 25, 50, 99, 75, 5]})
print(test_df)
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)
# Testing End

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.head())
print(reshaped_df.count())
print(reshaped_df.describe())

reshaped_df.fillna(0, inplace=True)
print(reshaped_df.head())
print(reshaped_df.isna().values.any())

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()

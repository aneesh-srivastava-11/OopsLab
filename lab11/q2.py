# Pandas - Loading Data
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())

# Pandas - Selection & Filtering
print(df['col'])
print(df.loc[0])
print(df.iloc[0:2, 0:2])
print(df[df['col'] > 5])

# Pandas - Cleaning Data
df = df.dropna()
df = df.fillna(0)
print(df.isnull().sum())

# Pandas - Grouping
print(df.groupby('col').mean())
print(df.agg({'col': 'sum'}))

# Matplotlib - Basic Plotting
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.scatter([1, 2, 3], [4, 5, 6])
plt.bar([1, 2, 3], [4, 5, 6])
plt.show()

# Matplotlib - Customization
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Plot')
plt.legend(['Data'])
plt.subplot(1, 2, 1)

# Integration - Pandas + Matplotlib
df['col'].plot(kind='line')
plt.plot(df['col'])
plt.show()

# Exercise: Group by duration and plot
df.groupby('Duration')['Pulse'].mean().plot(kind='bar')
plt.title('Mean Pulse by Duration')
plt.xlabel('Duration')
plt.ylabel('Mean Pulse')
plt.show()

# NumPy - Array Creation
import numpy as np

a = np.array([1, 2, 3])
print(np.zeros(5))
print(np.ones((2, 3)))
print(np.arange(10))

# NumPy - Indexing & Attributes
print(a.shape, a.dtype, a.ndim)
print(a[0], a[1:3], a[-1])

b = np.array([[1, 2], [3, 4]])
print(b[0, 1])

# NumPy - Operations
print(a + 2)
print(a * a)
print(np.mean(a))
print(np.sum(a))
print(np.array([1, 2]) + np.array([[10], [20]]))

# NumPy - Shape & Random
a = np.arange(6)
print(a.reshape(3, 2))
np.random.seed(42)
print(np.random.rand(3, 3))

# Pandas - Series & DataFrame
import pandas as pd

s = pd.Series([1, 2, 3])
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(s)
print(df)

# Exercise
arr = np.random.rand(3, 3)
means = np.mean(arr, axis=1)
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
print("Row Means:", means)

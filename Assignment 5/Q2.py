"""
Q2) Questions on Basic NumPy Array:
    a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5])
    b) Find the most frequent value and their indice(s) in the following arrays:
        i.  x = np.array([1,2,3,4,5,1,2,1,1,1])
        ii. y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
"""

import numpy as np

# a)
arr = np.array([1, 2, 3, 6, 4, 5])
print(arr[::-1])

# b) i)
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
values, counts = np.unique(x, return_counts=True)
most_frequent_x = values[np.argmax(counts)]
indices_x = np.where(x == most_frequent_x)[0]
print("Most frequent value in x:", most_frequent_x)
print("Indices in x:", indices_x)

# b) ii)
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
values, counts = np.unique(y, return_counts=True)
most_frequent_y = values[np.argmax(counts)]
indices_y = np.where(y == most_frequent_y)[0]
print("Most frequent value in y:", most_frequent_y)
print("Indices in y:", indices_y)

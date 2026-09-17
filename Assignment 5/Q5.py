"""
Q5) Create a 2-D Array of three rows and four columns, named ucs420_Nikunj with the
following values - 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. Compute the mean,
median, max, min, unique elements. Reshape the array to four rows and three columns
and name it as reshaped_ucs420_Nikunj. Resize the array to two rows and three columns
and name it as resized_ucs420_Nikunj.
"""

import numpy as np

ucs420_Nikunj = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35]).reshape(3, 4)
print("ucs420_Nikunj:")
print(ucs420_Nikunj)

print("Mean:", np.mean(ucs420_Nikunj))
print("Median:", np.median(ucs420_Nikunj))
print("Max:", np.max(ucs420_Nikunj))
print("Min:", np.min(ucs420_Nikunj))
print("Unique elements:", np.unique(ucs420_Nikunj))

reshaped_ucs420_Nikunj = ucs420_Nikunj.reshape(4, 3)
print("reshaped_ucs420_Nikunj (4x3):")
print(reshaped_ucs420_Nikunj)

resized_ucs420_Nikunj = np.resize(ucs420_Nikunj, (2, 3))
print("resized_ucs420_Nikunj (2x3):")
print(resized_ucs420_Nikunj)

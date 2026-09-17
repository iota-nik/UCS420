"""
Q4) Write program to create an 1-D NumPy array named Nikunj with evenly spaced 25
numbers from 10 to 100 using linspace(). Print the dimensions of the array, shape,
total elements, the data type of each element and total number of bytes consumed by
the array. Find the transpose of this array using reshape() attribute. Can we do the
same with T attribute?
"""

import numpy as np

Nikunj = np.linspace(10, 100, 25)

print("Array:", Nikunj)
print("Dimensions (ndim):", Nikunj.ndim)
print("Shape:", Nikunj.shape)
print("Total elements (size):", Nikunj.size)
print("Data type:", Nikunj.dtype)
print("Total bytes (nbytes):", Nikunj.nbytes)

transposed_reshape = Nikunj.reshape(25, 1)
print("Transposed using reshape():")
print(transposed_reshape)

transposed_T = Nikunj.T
print("Using T attribute:")
print(transposed_T)
print("Shape after .T:", transposed_T.shape)

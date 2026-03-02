# Program 2a: Demonstrate basic operations, unary and binary operations in numpy array

import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

print("Addition:", array1 + array2)
print("Square root (Unary):", np.sqrt(array1))
print("Dot product (Binary):", np.dot(array1, array2))

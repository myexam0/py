# Program 1b: Demonstrate indexing in numpy array

import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])
array_2d = np.array([[1, 2], [3, 4], [5, 6]])

print("Element at index2 (1D):", array_1d[2])
print("Element at (1,1) (2D):", array_2d[1, 1])
print("Row 1(2D):", array_2d[1, :])

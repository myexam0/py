# Program 2b: Demonstrate vertical and horizontal stacking and splitting

import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

v_stack = np.vstack((array1, array2))
h_stack = np.hstack((array1, array2))
v_split = np.vsplit(v_stack, 2)

print("Vertical stack:\n", v_stack)
print("Horizontal stack:\n", h_stack)

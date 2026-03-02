# Program 4a: Apply linear algebra methods on numpy array

import numpy as np

matrix = np.array([[2, 1], [1, 3]])

det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
transpose = matrix.T

print("Matrix:", matrix)
print("Determinant:", det)
print("Inverse:\n", inv)
print("Eigenvalues:", eigenvalues)
print("Transpose:\n", transpose)

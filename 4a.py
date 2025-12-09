import numpy as np
matrix=np.array([[2,1],[1,3]])
det=np.linalg.det(matrix)
inv=np.linalg.inv(matrix)
eigenvalues,eigenvectors=np.linalg.eig(matrix)
tranpose=matrix.T
print("Matrix:",matrix)
print("Determiant:",det)
print("Inverse:\n",inv)
print("Eigenvalues:",eigenvalues)
print("Transpose:\n",tranpose)

import pandas as pd

# Scalar values with default index
scalar_series_default = pd.Series(5, index=[0, 1, 2, 3])
print("Scalar Series with Default Index:\n", scalar_series_default)

# Scalar values with predefined index
predefined_index = pd.Series(10, index=['a', 'b', 'c', 'd'])
print("\nScalar Series with Predefined Index:\n", predefined_index)

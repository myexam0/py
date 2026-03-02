# Program 5a: Create pandas series with scalar values, default and predefined index

import pandas as pd

Scalar_Series_default = pd.Series(5, index=[0, 1, 2, 3])
print("Scalar Series with default Index:\n", Scalar_Series_default)

predefined_index = pd.Series(10, index=['a', 'b', 'c', 'd'])
print("\nScalar Series with predefined Index:\n", predefined_index)

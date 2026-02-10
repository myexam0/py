import pandas as pd
import numpy as np

# Dictionary to Series
dict_series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print("Dictionary Series:\n", dict_series)

# ndarray to Series
ndarray_series = pd.Series(np.array([10, 20, 30, 40]))
print("\nndarray Series:\n", ndarray_series)

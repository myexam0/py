# Program 5b: Create Dictionary series, ndarray series

import pandas as pd
import numpy as np

dict_series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print("Dictionary Series:\n", dict_series)

ndarray_Series = pd.Series(np.array([10, 20, 30, 40]))
print("\nndarray series:\n", ndarray_Series)

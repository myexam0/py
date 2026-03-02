# Program 5d: Create DataFrame from three series and from 2D array

import pandas as pd
import numpy as np

Series1 = pd.Series([1, 2, 3], name='a')
Series2 = pd.Series([4, 5, 6], name='b')
Series3 = pd.Series([7, 8, 9], name='c')

df_from_Series = pd.concat([Series1, Series2, Series3], axis=1)
print("DataFrame from three series:\n", df_from_Series)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_from_array = pd.DataFrame(array_2d, columns=['a', 'b', 'c'])
print("\nDataFrame from 2D array:\n", df_from_array)

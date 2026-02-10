import pandas as pd
import numpy as np

# Creating three Series
series1 = pd.Series([1, 2, 3], name='A')
series2 = pd.Series([4, 5, 6], name='B')
series3 = pd.Series([7, 8, 9], name='C')

# Creating DataFrame from three Series
df_from_series = pd.concat([series1, series2, series3], axis=1)
print("DataFrame from Three Series:\n", df_from_series)

# Creating a DataFrame from a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_from_array = pd.DataFrame(array_2d, columns=['A', 'B', 'C'])
print("\nDataFrame from 2D Array:\n", df_from_array)

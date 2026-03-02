# Program 5c: Create DataFrame with two dictionaries

import pandas as pd

dic1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dic2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}

df = pd.DataFrame([dic1, dic2])
print("DataFrame from two dictionaries:\n", df)

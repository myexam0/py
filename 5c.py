import pandas as pd

# Two dictionaries
dict1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dict2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}

# Creating DataFrame from the dictionaries
df = pd.DataFrame([dict1, dict2])
print("DataFrame from two dictionaries:\n", df)

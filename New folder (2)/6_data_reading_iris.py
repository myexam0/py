# Program 6: Reading data from text files, Excel and web - Iris dataset analysis

import pandas as pd

# Reading from a text file (CSV)
text_data = pd.read_csv('one.csv')
print("Text file data:\n", text_data.head())

# Reading from an excel file
# excel_data = pd.read_excel('data.xlsx')
# print("\nExcel data:\n", excel_data.head())

# Reading from a web URL (Iris dataset from UCI)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = pd.read_csv(url, header=None, names=['SepalLength', 'Sepalwidth', 'petalLength', 'petelwidth', 'spacies'])

# Descriptive analytics on this data
print("\nIris data description:\n", iris_data.describe())

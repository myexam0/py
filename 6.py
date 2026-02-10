import pandas as pd

# Reading from a text file (CSV)
text_data = pd.read_csv('data.txt')
print("Text File Data:\n", text_data.head())

# Reading from an Excel file
excel_data = pd.read_excel('data.xlsx')
print("\nExcel Data:\n", excel_data.head())

# Reading from a web URL (Iris dataset from UCI)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = pd.read_csv(url, header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'])

# Descriptive analytics on Iris data
print("\nIris Data Description:\n", iris_data.describe())

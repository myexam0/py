# Program 7a: Univariate analysis - Frequency, Mean, Median, Mode, Variance, Standard Deviation

import pandas as pd

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
columns = ['pregnacies', 'Glucose', 'Bloodpressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=columns)

mean = data['Glucose'].mean()
median = data['Glucose'].median()
mode = data['Glucose'].mode()[0]
variance = data['Glucose'].var()
std_dev = data['Glucose'].std()

frequency = data['Outcome'].value_counts()

print(f"Mean:{mean}, Median:{median}, Mode:{mode}, Variance:{variance}, Std Dev:{std_dev}")
print(f"Frequency of Outcome:\n{frequency}")

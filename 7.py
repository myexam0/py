import pandas as pd
# Load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=columns)

# Univariate analysis for 'Glucose'
mean = data['Glucose'].mean()
median = data['Glucose'].median()
mode = data['Glucose'].mode()[0]
variance = data['Glucose'].var()
std_dev = data['Glucose'].std()

# Frequency of 'Outcome'
frequency = data['Outcome'].value_counts()

print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Variance: {variance}, Std Dev: {std_dev}")
print(f"Frequency of Outcome:\n{frequency}")


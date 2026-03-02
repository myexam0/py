# Program 7b: Bivariate analysis - Linear and logistic regression modelling

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv',
                   names=['Pregnancies', 'Glucose', 'BloodPressure', 'skinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])

# Linear Regression
x = data[['BMI']]
y = data['Glucose']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("Linear MSE:", mean_squared_error(y_test, LinearRegression().fit(x_train, y_train).predict(x_test)))

# Logistic Regression
x = data[['Glucose', 'BMI']]
y = data['Outcome']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("Logistic Accuracy:", accuracy_score(y_test, LogisticRegression().fit(x_train, y_train).predict(x_test)))

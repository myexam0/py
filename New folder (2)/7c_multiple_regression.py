# Program 7c: Multiple Regression analysis

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=columns)

x = data[['Pregnancies', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = data['Glucose']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

reg_model = LinearRegression().fit(x_train, y_train)
y_pred = reg_model.predict(x_test)

print("Multiple Regression MSE:", mean_squared_error(y_test, y_pred))


import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

data = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv', names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])
X = data[['BMI']]; y = data['Glucose']; X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Linear MSE:", mean_squared_error(y_test, LinearRegression().fit(X_train, y_train).predict(X_test)))
X = data[['Glucose', 'BMI']]; y = data['Outcome']; X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Logistic Accuracy:", accuracy_score(y_test, LogisticRegression().fit(X_train, y_train).predict(X_test)))

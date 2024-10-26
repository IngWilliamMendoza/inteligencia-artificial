import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df_salary = pd.read_excel("../Data_sets/Salary.xlsx")
x = df_salary[['YearsExperience']]
y = df_salary['Salary']

model = LinearRegression()

model.fit(x, y)
y_predit = model.predict(x)
r2 = r2_score(y, y_predit)

plt.figure(figsize = (10,6))
plt.scatter(x,y, color='blue', label='Puntos de dispersion')
plt.plot(x, y_predit, color='red', label='Linear Regression')
plt.title("Regresion Lineal: Salario vs Años de experiencia")
plt.xlabel("Anios de experiencia")
plt.ylabel("Salario")
plt.legend()
plt.grid(True)
plt.show()

print(f"Ecuacion de la regresion lineal: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")




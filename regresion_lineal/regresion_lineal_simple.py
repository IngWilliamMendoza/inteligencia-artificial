# -*- coding: utf-8 -*-
"""
regresion_lineal_simple.py
--------------------------
Este script realiza una regresión lineal simple utilizando pandas y otras bibliotecas de Python.

Autor: IngWilliamMendoza
Fecha: 2023-10-05
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df_salary = pd.read_csv('../data_sets/Salary_Data.csv')
X = df_salary.iloc[:, :-1].values
y = df_salary.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)

regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred = regression.predict(X_test)

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salario vs Años de Experiencia (Conjunto de Entrenamiento)')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.show()

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salario vs Años de Experiencia (Conjunto de Testing)')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.show()

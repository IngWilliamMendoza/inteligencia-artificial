import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# EJERCICIO DE REGRESION LINEAL

# df_salary = pd.read_excel("../Data_sets/Salary.xlsx")
# x = df_salary[['YearsExperience']]
# y = df_salary['Salary']
#
# model = LinearRegression()
#
# model.fit(x, y)
# y_predit = model.predict(x)
# r2 = r2_score(y, y_predit)
#
# plt.figure(figsize = (10,6))
# plt.scatter(x,y, color='blue', label='Puntos de dispersion')
# plt.plot(x, y_predit, color='red', label='Linear Regression')
# plt.title("Regresion Lineal: Salario vs Años de experiencia")
# plt.xlabel("Anios de experiencia")
# plt.ylabel("Salario")
# plt.legend()
# plt.grid(True)
# plt.show()
#
# print(f"Ecuacion de la regresion lineal: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
# print(f"R2 score: {r2: .2f}")

# EJERCICIO DE CALIDAD DEL AIRE

df_air_quality = pd.read_csv('../Data_sets/air_quality_no2.csv', index_col=0, parse_dates=True)

# crear grafica con los datos del data_set
# df_air_quality.plot()
# plt.show()

# crear grafica de una columna o variable especifica
# df_air_quality['station_paris'].plot()
# plt.show()

# crear grafica en base a 2 variables
# df_air_quality.plot.scatter(x='station_london', y='station_paris', alpha=0.5)
# plt.show()

# Obtener los tipos de graficas que tenemos de plot

# listadoGraficas = [ method_name for method_name in dir(df_air_quality.plot) if not method_name.startswith("_")]
# print(listadoGraficas)

# crear un diagrama de caja
# df_air_quality.plot.box()
# plt.show()

# axs = df_air_quality.plot.area(figsize=(12,4), subplots=True )
# plt.show()

fig, axs = plt.subplots(figsize=(12, 4))
df_air_quality.plot.area(ax=axs, color='blue')

axs.set_ylabel('NO$_2$ concentration')
fig.savefig('../Figures/air_quality_no2.png')



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from IPython.core.pylabtools import figsize

df_edad_precio_seguro = pd.read_csv('../Data_sets/dataset_edad_precio_seguro.csv')

x = df_edad_precio_seguro[['Edad']]
y = df_edad_precio_seguro['PrecioSeguro']

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)
r2 = r2_score(y, y_pred)


plt.figure(figsize(8,6))
plt.scatter(x,y, color='blue', label='Puntos de datos')
plt.plot(x, y_pred, color='red', label='Linear Regression')
plt.title('Regresion lineal de precio seguro vs edad')
plt.ylabel('Precio seguro')
plt.xlabel('Edad')
plt.legend()
plt.grid(True)

plt.show()


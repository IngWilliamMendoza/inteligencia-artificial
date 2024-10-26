import pandas as pd

# crear un dataframe

# df = pd.DataFrame(
# 	{
# 		"Name": [
# 			"Braund, Mr. Owen Harris",
# 			"Allen, Mr. William Henry",
# 			"Bonnell, Miss. Elizabeth",
# 		],
# 		"Age": [22, 35, 58],
# 		"Sex": ["M", "F", "M"],
# 	}
# )
#
# print(df)
#
# # importar y manipular un dataframe
#
# df_venta_productos = pd.read_excel('../Data_sets/ventas_productos.xlsx')
# df_venta_productos['Ventas_Totales'] = df_venta_productos['Precio_Unitario']  * df_venta_productos['Cantidad']
# print(df_venta_productos)

# df_inventarios = pd.read_excel('../Data_sets/inventario.xlsx')
# productos_bajo_stock = df_inventarios[ df_inventarios['Cantidad_Disponible'] < df_inventarios['Stock_Mínimo'] ]
#
# print(productos_bajo_stock)

# obtener el maximo de un Series
# df_stock_maximo = df_inventarios['Cantidad_Disponible'].max()
# print(f'la cantidad maxima de stock es {df_stock_maximo}')

# df_inventarios_describe = df_inventarios.describe()
# print(df_inventarios_describe)

# importar datos desde un csv
df_titanic = pd.read_csv('../Data_sets/titanic.csv')

# ver las primeras filas del dataFrame
# print(df_titanic.head(8))

# ver las ultimas filas del dataFrame
# print(df_titanic.tail(5))

# ver los tipos de cada columna del dataFrame
#print(df_titanic.dtypes)

# convertir un dataFrame a excel
df_titanic.to_excel("../Data_sets/titanic.xlsx", sheet_name='passengers', index=False )
df_titanic_excel = pd.read_excel("../Data_sets/titanic.xlsx", sheet_name='passengers')
print(df_titanic_excel)

# ver un resumen tecnico de un DataFrame



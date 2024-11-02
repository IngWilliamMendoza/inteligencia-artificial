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

# df_estudiantes = pd.read_excel('../Data_sets/calificaciones_estudiantes.xlsx')
# df_estudiante_honor = df_estudiantes
#
# print(df_estudiantes)

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
# df_titanic.to_excel("../Data_sets/titanic.xlsx", sheet_name='passengers', index=False )
# df_titanic_excel = pd.read_excel("../Data_sets/titanic.xlsx", sheet_name='passengers')
# print(df_titanic_excel)

# ver un resumen tecnico de un DataFrame
#print(df_titanic.info())

# obtener el numero de filas y columnas de un dataFrame
# print(f"numero de filas y columnas {df_titanic.shape}")
# print(f"numero de filas del Series Age {df_titanic['Age'].shape}")

# crear un dataFrame apartir de un dataFrame, solo tomara las 5 primeras filas
# df_age_sex = df_titanic[["Age", "Sex"]].head(5)
# print(df_age_sex)

# crear un dataFrame filtrando los valores
# df_above_35 = df_titanic[df_titanic["Age"] > 35]
# print(df_above_35)

# filtrar un dataFrame con el condicional isIn()
# df_titanic_class23 = df_titanic[df_titanic['Pclass'].isin([2,3])]
# print(df_titanic_class23)

# filtar un dataFrame por campos not null
# age_no_na = df_titanic[df_titanic["Age"].notna()]
# print(age_no_na)

# Seleccionar filas y columnas expecificas de un DataFrame
# adult_names = df_titanic.loc[df_titanic["Age"] > 35, "Name"]
# print(adult_names.head())

# Seleccionar filar y columnas por index
df_titanic_index = df_titanic.iloc[5:15, 2:5]
# print(df_titanic_index)

# Sobre escribir unos campos especificos por index
# print(df_titanic_index.info())
df_titanic_index.iloc[0:3, 1] = "anonymous"
print(df_titanic_index)
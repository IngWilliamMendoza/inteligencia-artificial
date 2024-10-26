import pandas as pd

# crear un dataframe

df = pd.DataFrame(
	{
		"Name": [
			"Braund, Mr. Owen Harris",
			"Allen, Mr. William Henry",
			"Bonnell, Miss. Elizabeth",
		],
		"Age": [22, 35, 58],
		"Sex": ["M", "F", "M"],
	}
)

print(df)

# importar y manipular un dataframe

df_venta_productos = pd.read_excel('../Data_sets/ventas_productos.xlsx')
df_venta_productos['Ventas_Totales'] = df_venta_productos['Precio_Unitario']  * df_venta_productos['Cantidad']
print(df_venta_productos)



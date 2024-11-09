# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


# documentacion preprocessing ->  https://scikit-learn.org/1.5/modules/preprocessing.html
# documentacion imputer -> https://scikit-learn.org/1.5/modules/generated/sklearn.impute.SimpleImputer.html

# importar el dataset
df_data = pd.read_csv('../Data_sets/Data.csv')

# declarar variable independiente y dependiente
X = df_data.iloc[:, :-1].values
y = df_data.iloc[:, 3].values

# limpiar los datos - Imputer de valores faltantes con la media
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean" )
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])



# Codificar datos categoricos ordinales
labelencoder_purchased = LabelEncoder()
y = labelencoder_purchased.fit_transform(y)

# Codificar datos categoricos no ordinales
labelencoder_countries = LabelEncoder()
X[:, 0] = labelencoder_countries.fit_transform(X[:, 0])

ct_countries = ColumnTransformer(
        transformers=[('encoder', OneHotEncoder(),[0])], remainder='passthrough' 
    )


X = ct_countries.fit_transform(X)

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)




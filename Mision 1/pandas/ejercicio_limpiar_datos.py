# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# documentacion preprocessing ->  https://scikit-learn.org/1.5/modules/preprocessing.html
# documentacion imputer -> https://scikit-learn.org/1.5/modules/generated/sklearn.impute.SimpleImputer.html

# importar el dataset
df_data = pd.read_csv('../Data_sets/Data.csv')

# declarar variable independiente y dependiente
X = df_data.iloc[:, :-1].values
y = df_data.iloc[:, 3].values

# limpiar los datos
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean" )
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
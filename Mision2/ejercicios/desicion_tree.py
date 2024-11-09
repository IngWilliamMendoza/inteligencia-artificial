#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:27:14 2024

@author: wamendoza
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

df_house_prices = pd.read_csv('../Data_sets/house_prices_large.csv')

mediana_precio = df_house_prices['Price'].median()
df_house_prices['CategoriaPrecio'] = pd.cut(df_house_prices['Price'], bins=[
                                            0, mediana_precio, df_house_prices['Price'].max()], labels=[0, 1]).astype(int)

X = df_house_prices[['House_Size']]
y = df_house_prices['CategoriaPrecio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred =model.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt='g')

plt.xlabel('Prediccion')
plt.ylabel('Real')
plt.title('Matriz de la confusion - Desicion Tree')
plt.xticks([0.5, 1.5], ['Bajo', 'Alto'])
plt.yticks([0.5, 1.5], ['Bajo', 'Alto'])
plt.show()

print(classification_report(y_test, y_pred, target_names=['Bajo', 'Alto']))



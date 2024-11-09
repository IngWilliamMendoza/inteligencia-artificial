#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:48:49 2024

@author: wamendoza
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

#importar el dataset
data = pd.read_csv('../Data_sets/dataset_experiencia_salario.csv')
print(data)

#crear el dataframe
df = pd.DataFrame(data)

#agregar categoria salario
df['CategoriaSalario'] = pd.cut(df['Salario'], bins=[0,70000,150000], labels=['Bajo', 'Alto'])

# asignar variable independiente y dependiente
X = df[['Años de Experiencia']]
y = df['CategoriaSalario']

# mapear categoria salario
y_numeric = y.map({'Bajo': 0, 'Alto':1})

# crear variables de test y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y_numeric, test_size=0.3, random_state=42)

# crear el arbol de decision
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

y_pred = tree_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)


plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Bajo', 'Alto'], yticklabels=['Bajo', 'Alto'])
plt.xlabel('Predicciones')
plt.ylabel('Real')
plt.title('Matriz de Confusion')
plt.show()


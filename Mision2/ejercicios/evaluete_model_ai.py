import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from model_utils import train_model, evaluate_model, compare_models

df_house_prices = pd.read_csv('../Data_sets/house_prices_large.csv')
median_price = df_house_prices['Price'].median()
df_house_prices['CategoryPrice'] = pd.cut(df_house_prices['Price'],
                                          bins=[0, median_price, df_house_prices['Price'].max()], labels=[0, 1])
X = df_house_prices[['House_Size']]
y = df_house_prices['CategoryPrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Árbol de Decisión": DecisionTreeClassifier(random_state=42),
    "Regresión Logística": LogisticRegression()
}

conf_matrices = {}
for model_name, model in models.items():
    trained_model = train_model(model, X_train, y_train)
    conf_matrices[model_name] = evaluate_model(trained_model, X_test, y_test, model_name)

compare_models(conf_matrices)

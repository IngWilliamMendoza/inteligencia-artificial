import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# entrenar un modelo
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

# Generar predicciones y métricas
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(f"\nReporte de clasificación para {model_name}:")
    print(classification_report(y_test, y_pred, target_names=['Bajo', 'Alto']))
    plot_confusion_matrix(conf_matrix, f'Matriz de Confusión - {model_name}')
    return conf_matrix

# Graficar la matriz de confusión
def plot_confusion_matrix(conf_matrix, title):
    plt.figure(figsize=(6, 5))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt='g')
    plt.xlabel('Predicción')
    plt.ylabel('Real')
    plt.title(title)
    plt.xticks([0.5, 1.5], ['Bajo', 'Alto'])
    plt.yticks([0.5, 1.5], ['Bajo', 'Alto'])
    plt.show()

# Comparar modelos
def compare_models(conf_matrices):
    accuracies = {}
    for model_name, conf_matrix in conf_matrices.items():
        correct_predictions = conf_matrix[0, 0] + conf_matrix[1, 1]
        total_predictions = conf_matrix.sum()
        accuracies[model_name] = correct_predictions / total_predictions

    best_model = max(accuracies, key=accuracies.get)
    print(f"\nEl modelo más preciso es {best_model} con una precisión de {accuracies[best_model]:.2f}")
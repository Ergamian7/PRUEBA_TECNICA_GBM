import sys
import pandas as pd
from keras.models import load_model

# Cargar el modelo entrenado
model = load_model('customer_classification_model')

# Función para clasificar clientes
def classify_customers(frequency, spending_habit, max_spending):
    # Utilizar solo la característica 'frequency' como entrada
    data = pd.DataFrame({'frequency': [frequency]})
    
    # Realizar predicciones con el modelo cargado
    predictions = model.predict(data)
    
    # Interpretar las predicciones y devolver la clase correspondiente
    class_labels = ['bajo', 'medio', 'alto']
    predicted_class_index = predictions.argmax(axis=1)[0]
    return class_labels[predicted_class_index]

# Guardar la salida estándar en un archivo
original_stdout = sys.stdout
with open('test_case_1_output.txt', 'w') as f:
    sys.stdout = f  # Cambiar la salida estándar al archivo

    # Aquí va tu código para ejecutar la prueba
    frequency = 10  # Ejemplo de frecuencia de compra
    spending_habit = 500  # Ejemplo de hábito de gasto
    max_spending = 1000  # Ejemplo de cantidad máxima gastada
    classification = classify_customers(frequency, spending_habit, max_spending)
    print("Clasificación del cliente:", classification)

    # Restaurar la salida estándar original
    sys.stdout = original_stdout

print("La salida de la prueba se ha guardado en 'test_case_1_output.txt'")


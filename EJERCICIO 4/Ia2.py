import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

# Cargar los datos del archivo "data_customer_classification.xlsx".
data = pd.read_excel(r"C:\Users\ermiranda\OneDrive - GBM Corporacion\Desktop\EJERCICIO 4\data_customer_classification.xlsx")

# Preprocesar los datos según sea necesario

# 1. Eliminar columnas no necesarias (customer_id, trans_date)
data.drop(columns=['customer_id', 'trans_date'], inplace=True)

# 2. Convertir la columna 'tran_amount' en una etiqueta categórica
def categorize_amount(amount):
    if amount < 100:
        return 'bajo'
    elif amount < 500:
        return 'medio'
    else:
        return 'alto'

data['category'] = data['tran_amount'].apply(categorize_amount)

# 3. Convertir las etiquetas categóricas en números usando LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['category'])

# Convertir los valores de la columna 'tran_amount' a números flotantes
data['tran_amount_numeric'] = pd.to_numeric(data['tran_amount'], errors='coerce')

# Eliminar filas con valores nulos en 'tran_amount_numeric'
data = data.dropna(subset=['tran_amount_numeric'])

# 4. Dividir los datos en características (X) y etiquetas (y).
X = data.drop(columns=['tran_amount', 'category'])  # Eliminar 'tran_amount' y 'category'
y = data['category']  # Usar la categoría en lugar del monto

# 5. Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Datos de entrada en X_test:")
print(X_test.head())

# Imprimir X_train para verificar su contenido antes de escalarlo
print("Contenido de X_train antes de escalar:")
print(X_train.head())

# Verificar que los datos se dividan correctamente en los conjuntos de entrenamiento y prueba
print("Tamaño de X_train:", X_train.shape)
print("Tamaño de X_test:", X_test.shape)
print("Tamaño de y_train:", y_train.shape)
print("Tamaño de y_test:", y_test.shape)

# Asegurarse de que los datos estén en el formato correcto y no contengan valores faltantes
print("Valores nulos en X_train:", X_train.isnull().sum())
print("Valores nulos en X_test:", X_test.isnull().sum())

# Revisar si la función categorize_amount y la asignación de etiquetas se realizan correctamente
print("Ejemplo de categorías generadas:")
print(data[['tran_amount', 'category']].head())

# 6. No es necesario escalar los datos

# Convertir los datos de Pandas a Numpy arrays y asegurarse de que estén en formato float32
X_train_np = np.array(X_train).astype('float32')

# Usar las etiquetas codificadas 'y_train' en lugar de 'y_train_numeric'
y_train_numeric = label_encoder.transform(y_train)
y_train_np = np.array(y_train_numeric).astype('float32')

# 7. Definir el modelo de Keras
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train_np.shape[1]))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))  # Capa de salida con 3 neuronas para las 3 categorías

# 8. Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 9. Entrenar el modelo
model.fit(X_train_np, y_train_np, epochs=50, batch_size=32, validation_split=0.1)

# 10. Evaluar el modelo en el conjunto de prueba
X_test_np = np.array(X_test).astype('float32')  # Convertir X_test a numpy array
y_test_numeric = label_encoder.transform(y_test)  # Codificar las etiquetas de prueba
y_test_np = np.array(y_test_numeric).astype('float32')  # Convertir y_test a numpy array
loss, accuracy = model.evaluate(X_test_np, y_test_np)
print(f'Accuracy on test set: {accuracy}')

# 11. Guardar el modelo entrenado
model.save('customer_classification_model')




## Ejercicio 4: Modelo de Clasificación de Clientes
En este ejercicio, se desarrolló un modelo de clasificación utilizando Keras que tiene en cuenta la frecuencia de compra de los clientes, sus hábitos de gasto y la cantidad máxima que gastan en el almacenar. El objetivo del modelo es clasificar a los clientes en tres categorías: bajo, medio y alto valor.

## Contenido del Repositorio
data_customer_classification.xlsx: Archivo Excel que contiene los datos necesarios para entrenar el modelo.
my_model.py: Archivo Python que contiene el código para cargar los datos, preprocesarlos, entrenar el modelo y guardar el modelo entrenado.
guardar_prueba.py: Archivo Python que carga el modelo entrenado y realiza una prueba de clasificación de un cliente.
test_case_1_output.txt: Archivo de salida que contiene el resultado de la prueba realizada en guardar_prueba.py.
readme.md: Este archivo, que proporciona documentación sobre el proceso del ejercicio.

## Instrucciones de Uso
Entrenamiento del Modelo: Ejecutar el script my_model.py para entrenar el modelo. Este script carga los datos del archivo data_customer_classification.xlsx, preprocesa los datos, define y entrena el modelo utilizando Keras, y finalmente guarda el modelo entrenado en un archivo llamado customer_classification_model.

## bash
Copy code
python my_model.py

Prueba de Clasificación: Una vez que el modelo está entrenado y guardado, se puede realizar una prueba de clasificación de un cliente ejecutando el script guardar_prueba.py.

## bash
Copy code
python guardar_prueba.py
Esto generará un archivo test_case_1_output.txt que contiene el resultado de la clasificación del cliente.

## Dependencias
Python 3.9
## Bibliotecas Python:
pandas
numpy
scikit-learn
keras
## Bibliotecas Instaladas
Para verificar las bibliotecas instaladas en tu entorno, puedes utilizar el siguiente comando:

bash
Copy code
pip list

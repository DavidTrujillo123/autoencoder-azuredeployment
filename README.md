# Proyecto de Detecci´no de Fraude con Autoencoder

Este proyecto implementa un modelo de autoencoder para la detección de transacciones fraudulentas en tarjetas de crédito. El modelo ha sido entrenado y desplegado utilizando Flask y se puede acceder a través de una interfaz web.

### Descripción de Archivos y Carpetas

- **app.py**: Archivo principal de la aplicación Flask. Contiene el código para cargar el modelo, manejar las solicitudes y renderizar las plantillas HTML.
- **autoencoder_model.h5**: Archivo del modelo de autoencoder entrenado.
- **README.md**: Archivo de documentación del proyecto.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar la aplicación.
- **static/css/style.css**: Archivo CSS para los estilos de la aplicación web.
- **templates/home.html**: Página principal de la aplicación web donde los usuarios pueden ingresar datos.
- **templates/result.html**: Página para mostrar los resultados de la predicción.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación Flask:

    ```bash
    python app.py
    ```

2. Abre tu navegador web y ve a `http://127.0.0.1:5000/`.

3. Ingresa los datos de la transacción en el formulario y haz clic en "Predecir" para ver el resultado.

## Descripción del Modelo

El modelo de autoencoder ha sido entrenado para detectar transacciones fraudulentas en un conjunto de datos de tarjetas de crédito. Utiliza una arquitectura de red neuronal con capas de codificación y decodificación para aprender la representación de las transacciones normales y detectar anomalías.

### Arquitectura del Modelo

- **Entrada**: 29 características de las transacciones.
- **Capas del Codificador**:
  - Capa densa con 20 neuronas y activación `tanh`.
  - Capa densa con 14 neuronas y activación `relu`.
- **Capas del Decodificador**:
  - Capa densa con 20 neuronas y activación `tanh`.
  - Capa densa con 29 neuronas y activación `relu`.

### Métricas de Evaluación

El modelo se evalúa utilizando varias métricas, incluyendo precisión, recall, F1-score y área bajo la curva ROC.

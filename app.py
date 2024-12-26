from flask import Flask, request, render_template
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# Cargar el modelo
model = load_model('autoencoder_model.h5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del formulario
    data = request.form['data']
    # Convertir los datos a un formato adecuado
    data = np.array([float(i) for i in data.split(',')]).reshape(1, -1)
    # Realizar la predicción
    prediction = model.predict(data)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
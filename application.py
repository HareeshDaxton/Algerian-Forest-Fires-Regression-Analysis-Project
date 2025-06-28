from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
scl = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    Temperature = float(request.form.get('Temperature'))
    RH = float(request.form.get('RH'))
    Ws = float(request.form.get('Ws'))
    Rains = float(request.form.get('Rains'))
    FFMC = float(request.form.get('FFMC'))
    DMC = float(request.form.get('DMC'))
    ISI = float(request.form.get('ISI'))
    Classes = float(request.form.get('Classes'))
    Region = float(request.form.get('Region'))

    # Predict
    input_data = np.array([[Temperature, RH, Ws, Rains, FFMC, DMC, ISI, Classes, Region]])
    scaled = scl.transform(input_data)
    result = ridge_model.predict(scaled)[0]

    return render_template('index.html', result=round(result, 2))

if __name__ == "__main__":
    app.run(debug=True)

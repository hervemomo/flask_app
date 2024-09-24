# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:27:11 2024

@author: herve
"""

from flask import Flask, render_template, request
import joblib
import numpy as np
# import os

app = Flask(__name__)

# Load the trained model
# model_path = os.path.join('model', 'model.pkl')
# model = joblib.load(model_path)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        size = float(request.form['size'])
        bedrooms = int(request.form['bedrooms'])
        features = np.array([[size, bedrooms]])
        prediction = model.predict(features)
        predicted_price = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f"Estimated Price: ${predicted_price}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)

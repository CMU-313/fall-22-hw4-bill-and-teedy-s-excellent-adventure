import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model84.pkl")
    rfc = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        Fedu = request.args.get('Fedu')
        Medu = request.args.get('Medu')
        Walc = request.args.get('Walc')
        absences = request.args.get('absences')
        age = request.args.get('age')
        failures = request.args.get('failures')
        freetime = request.args.get('freetime')
        goout = request.args.get('goout')
        health = request.args.get('health')

        query_df = pd.DataFrame({ 
                    'Fedu' : pd.Series(Fedu),
                    'Medu' : pd.Series(Medu), 
                    'Walc': pd.Series(Walc),
                    'absences': pd.Series(absences),
                    'age': pd.Series(age),
                    'failures': pd.Series(failures),
                    'freetime': pd.Series(freetime),
                    'goout': pd.Series(goout),
                    'health': pd.Series(health),
        })

        prediction = rfc.predict(query_df)
        return jsonify(np.ndarray.item(prediction))

# Query String: ?Fedu=1&Medu=3&Walc=4&absences=3&age=17&failures=0&freetime=4&goout=5&health=2
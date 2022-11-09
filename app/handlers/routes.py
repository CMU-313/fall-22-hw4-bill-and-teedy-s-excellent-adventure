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

    # modified from https://shzhangji.com/blog/2018/04/07/error-handling-in-restful-api/
    @app.route('/predict')
    def predict():
        if len(request.args) != 9:
            return 'len', 404
        Fedu = request.args.get('Fedu', type=int)
        if Fedu < 0 or Fedu > 4:
            return 'fedu', 404
        Medu = request.args.get('Medu', type=int)
        if Medu < 0 or Medu > 4:
            return 'medu', 404
        Walc = request.args.get('Walc', type=int)
        if Walc < 1 or Walc > 5:
            return 'walc', 404
        absences = request.args.get('absences', type=int)
        if absences < 0 or absences > 93:
            return 'absences', 404
        age = request.args.get('age', type=int)
        if age < 15 or age > 22:
            return 'age', 404
        failures = request.args.get('failures', type=int)
        if failures < 0 or failures > 5:
            return 'fails', 404
        freetime = request.args.get('freetime', type=int)
        if freetime < 1 or freetime > 5:
            return 'freetime', 404
        goout = request.args.get('goout', type=int)
        if goout < 1 or goout > 5:
            return 'goout', 404
        health = request.args.get('health', type=int)
        if health < 1 or health > 5:
            return 'health', 404

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
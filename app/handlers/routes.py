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

        class BadRequest(Exception):
            """Custom exception class to be thrown when local error occurs."""
            def __init__(self, message, status=404, payload=None):
                self.message = message
                self.status = status
                self.payload = payload

        # modified from https://shzhangji.com/blog/2018/04/07/error-handling-in-restful-api/
        @app.errorhandler(BadRequest)
        def handle_bad_request(error):
            """Catch BadRequest exception globally, serialize into JSON, and respond with 404."""
            payload = dict(error.payload or ())
            payload['status'] = error.status
            payload['message'] = error.message
            return jsonify(payload), 404

        #use entries from the query string here but could also use json
        if len(request.args) != 11:
            raise BadRequest ("incorrect number of fields")
        Fedu = request.args.get('Fedu', type=int)
        if Fedu < 0 or Fedu > 4:
            raise BadRequest ("bad or no input for Fedu")
        Medu = request.args.get('Medu', type=int)
        if Medu < 0 or Medu > 4:
            raise BadRequest ("bad or no input for Medu")
        Walc = request.args.get('Walc', type=int)
        if Walc < 1 or Walc > 5:
            raise BadRequest ("bad or no input for Walc")
        absences = request.args.get('absences', type=int)
        if absences < 0 or absences > 93:
            raise BadRequest ("bad or no input for absences")
        age = request.args.get('age', type=int)
        if age < 15 or age > 22:
            raise BadRequest ("bad or no input for age")
        failures = request.args.get('failures', type=int)
        if failures < 1 or failures > 5:
            raise BadRequest ("bad or no input for freetime")
        freetime = request.args.get('freetime', type=int)
        if freetime < 1 or freetime > 5:
            raise BadRequest ("bad or no input for freetime")
        goout = request.args.get('goout', type=int)
        if goout < 1 or goout > 5:
            raise BadRequest ("bad or no input for goout")
        health = request.args.get('health', type=int)
        if health < 1 or health > 5:
            raise BadRequest ("bad or no input for health")

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
import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        school = request.args.get('school')
        higher = request.args.get('higher')
        Mjob = request.args.get('Mjob')
        Fjob = request.args.get('Fjob')
        studytime = request.args.get('studytime')
        paid = request.args.get('paid')
        failures = request.args.get('failures')
        data = [[school], [higher], [Mjob], [Fjob], [studytime], [paid], [failures]]
        query_df = pd.DataFrame({
            'school': pd.Series(school),
            'higher': pd.Series(higher),
            'Mjob': pd.Series(Mjob),
            'Fjob': pd.Series(Fjob),
            'studytime': pd.Series(studytime),
            'paid': pd.Series(paid),
            'failures': pd.Series(failures),
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.asscalar(prediction))

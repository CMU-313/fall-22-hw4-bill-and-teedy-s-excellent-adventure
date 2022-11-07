import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model4.pkl")
    rfc = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        Fjob = request.args.get('Fjob')
        Mjob = request.args.get('Mjob')
        higher = request.args.get('higher')
        paid = request.args.get('paid')
        school = request.args.get('school')

        Fjob_health = 0
        Fjob_other = 0
        Fjob_services = 0
        Fjob_teacher = 0
        match Fjob:
            case "health": 
                Fjob_health = 1
            case "other":
                Fjob_other = 1
            case "services":
                Fjob_services = 1
            case "teacher":
                Fjob_teacher = 1
            case _:
                pass
        
        Mjob_health = 0
        Mjob_other = 0
        Mjob_services = 0
        Mjob_teacher = 0
        match Mjob:
            case "health": 
                Mjob_health = 1
            case "other":
                Mjob_other = 1
            case "services":
                Mjob_services = 1
            case "teacher":
                Mjob_teacher = 1
            case _:
                pass
        
        higher_yes = 0
        if higher == "yes":
            higher_yes = 1

        paid_yes = 0
        if paid == "yes":
            paid_yes = 1

        school_MS = request.args.get('school_MS')
        if school == "MS":
            school_MS = 1
        
        studytime = eval(request.args.get('studytime'))
        failures = eval(request.args.get('failures'))
       
        data = [[Fjob_health], [Fjob_other], 
                [Fjob_services], [Fjob_teacher],
                [Mjob_health], [Mjob_other],
                [Mjob_services], [Mjob_teacher],
                [failures], [higher_yes],
                [paid_yes], [school_MS], [studytime]]

        query_df = pd.DataFrame({ 
                    'Fjob_health' : pd.Series(Fjob_health),
                    'Fjob_other' : pd.Series(Fjob_other), 
                    'Fjob_services': pd.Series(Fjob_services),
                    'Fjob_teacher': pd.Series(Fjob_teacher),
                    'Mjob_health': pd.Series(Mjob_health),
                    'Mjob_other': pd.Series(Mjob_other),
                    'Mjob_services': pd.Series(Mjob_services),
                    'Mjob_teacher': pd.Series(Mjob_teacher),
                    'failures': pd.Series(failures),
                    'higher_yes': pd.Series(higher_yes),
                    'paid_yes': pd.Series(paid_yes),
                    'school_MS': pd.Series(school_MS),
                    'studytime': pd.Series(studytime)
        })

        # return str(query.columns.size)
        # return "" + query.columns[1] + query.columns[2] + query.columns[3] + "" + query.columns[4] + query.columns[5] + query.columns[6] + query.columns[7] + query.columns[8] + query.columns[9] + "" + query.columns[10] + query.columns[11]
        prediction = rfc.predict(query_df)
        return jsonify(np.asscalar(prediction))

# Query String: Fjob=health&Mjob=health&failures=0&higher=yes&paid=yes&school=MD&studytime=20
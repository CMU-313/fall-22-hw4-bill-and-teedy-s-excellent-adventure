import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing, neighbors, svm
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_selection import SelectFromModel
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
        df =pd.read_csv(os.path.join(this_dir, "../../data/ProductionData.csv"), sep=',')

        #####################
        df['qual_student'] = np.where(df['G3']>=15, 1, 0)
        df.drop(columns=['G3', 'G2', 'G1'], inplace=True) 

        df = pd.get_dummies(df, columns = df.select_dtypes(exclude=["number","bool_"]).columns)

        y = df['qual_student']
        col = df.columns.difference(['Fedu', 'Medu', 'Walc', 'absences', 'age', 'failures', 'freetime', 'goout', 'health'])
        X = df[df.columns.difference(col)]
        print(X.columns)

        result = rfc.score(X, y)

        # print('****Results****')
        # print("Accuracy: {:.4%}".format(rfc.score(X, y)))


        #####################

        return jsonify(result)
#! /usr/bin/env python
"""
Ejemplo de applicacion web que carga un pipeline de scikit-learn para predecir
"""
import json
from sklearn.externals import joblib
import pandas as pd
from flask import Flask, jsonify, request
from sklearn.base import BaseEstimator, TransformerMixin


# El pipeline guardado no contiene las definiciones de los transformadores
class ColumnExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, columns, output_type="matrix"):
        self.columns = columns
        self.output_type = output_type

    def transform(self, X, **transform_params):
        if isinstance(X, list):
            X = pd.DataFrame.from_dict(X)
        if self.output_type == "matrix":
            return X[self.columns].as_matrix()
        elif self.output_type == "dataframe":
            return X[self.columns]

    def fit(self, X, y=None, **fit_params):
        return self


with open('columnas_ames.json') as fname:
    pipeline_columnas = json.load(fname)

pipeline = joblib.load("pipeline_ames.pkl")
pipeline_dtypes = joblib.load("dtypes_ames.pkl")


def dict_a_df(obs, columnas, dtypes):
    obs_df = pd.DataFrame([obs])
    for col, dtype in dtypes.items():
        if col in obs_df.columns:
            obs_df[col] = obs_df[col].astype(dtype)
        else:
            obs_df[col] = None
    return obs_df


app = Flask(__name__)


@app.route('/predecir', methods=['POST'])
def predecir():
    observacion_dict = request.get_json()
    print("\nObservacion recibida. valores: {}".format(observacion_dict))
    obs_df = dict_a_df(observacion_dict, pipeline_columnas, pipeline_dtypes)
    prediccion = pipeline.predict(obs_df)[0]
    return jsonify({'prediccion': prediccion})


if __name__ == "__main__":
    app.run(debug=True, port=8000)

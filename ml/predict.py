# ml/predict.py

import os
import joblib
import pandas as pd
from ml.preprocess import preprocess_data

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "los_regression_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "feature_columns.pkl")

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)

def predict_length_of_stay(patient_dict: dict):

    df = pd.DataFrame([patient_dict])

    temp_path = os.path.join(BASE_DIR, "temp_patient.csv")
    df.to_csv(temp_path, index=False)

    X, _ = preprocess_data(temp_path)

    # 🔑 FORCE SAME COLUMN ORDER
    X = X[feature_columns]

    prediction = model.predict(X)[0]

    if os.path.exists(temp_path):
        os.remove(temp_path)

    rounded = int(round(prediction))
    return f"{rounded-1} to {rounded+1} days"

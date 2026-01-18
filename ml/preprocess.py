# ml/preprocess.py

import pandas as pd
import os
import joblib
from sklearn.preprocessing import LabelEncoder

TARGET_COL = "lengthofstay"
BASE_DIR = os.path.dirname(__file__)
FEATURES_PATH = os.path.join(BASE_DIR, "feature_columns.pkl")

def preprocess_data(path, save_features=False):
    df = pd.read_csv(path)

    # Drop non-ML columns
    df.drop(columns=["eid", "vdate"], inplace=True, errors="ignore")

    # Encode gender
    gender_encoder = LabelEncoder()
    df["gender"] = gender_encoder.fit_transform(df["gender"].astype(str))

    # Convert all columns to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Split target
    if TARGET_COL in df.columns:
        X = df.drop(TARGET_COL, axis=1)
        y = df[TARGET_COL]
    else:
        X = df.copy()
        y = None

    # 🔑 SAVE FEATURE ORDER DURING TRAINING
    if save_features:
        joblib.dump(list(X.columns), FEATURES_PATH)

    return X, y

# ml/patient_shap_explain.py

import os
import joblib
import shap
import pandas as pd
from ml.preprocess import preprocess_data

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "los_regression_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "feature_columns.pkl")
DATA_PATH = os.path.join(BASE_DIR, "../data/LengthOfStay.csv")

# -------------------------------------------------
# Load model and feature order
# -------------------------------------------------
model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)

# -------------------------------------------------
# Prepare background data for SHAP (training data)
# -------------------------------------------------
X_train, _ = preprocess_data(DATA_PATH)

# 🔑 Ensure SAME feature order as training
X_train = X_train[feature_columns]

background = X_train.sample(200, random_state=42)

# -------------------------------------------------
# SHAP Explainer (model-agnostic, stable)
# -------------------------------------------------
explainer = shap.Explainer(
    model.predict,
    background
)

# -------------------------------------------------
# MAIN FUNCTION (USED BY APP)
# -------------------------------------------------
def explain_single_patient(patient_dict: dict):
    """
    Generates SHAP explanation for a single patient
    Returns a DataFrame sorted by impact
    """

    # Convert dict → DataFrame
    df = pd.DataFrame([patient_dict])

    temp_path = os.path.join(BASE_DIR, "temp_patient.csv")
    df.to_csv(temp_path, index=False)

    # Preprocess
    X_patient, _ = preprocess_data(temp_path)

    # 🔑 FORCE SAME FEATURE ORDER
    X_patient = X_patient[feature_columns]

    # SHAP values
    shap_values = explainer(X_patient)

    # Cleanup temp file
    if os.path.exists(temp_path):
        os.remove(temp_path)

    # Build explanation DataFrame
    explanation = pd.DataFrame({
        "feature": X_patient.columns,
        "shap_value": shap_values.values[0]
    })

    explanation["abs_impact"] = explanation["shap_value"].abs()
    explanation = explanation.sort_values(
        by="abs_impact",
        ascending=False
    )

    return explanation

import joblib
import shap
import numpy as np
from preprocess import preprocess_data

# Load data
X, y, _ = preprocess_data("../data/LengthOfStay.csv")

# Load trained model
model = joblib.load("los_regression_model.pkl")

# Use KernelExplainer with model prediction function
# (This avoids XGBoost internal parsing issues)
explainer = shap.Explainer(
    model.predict,
    X.sample(200, random_state=42)  # background data
)

# Explain a sample (keep small for speed)
X_explain = X.sample(500, random_state=1)

shap_values = explainer(X_explain)

# Summary plot
shap.summary_plot(shap_values, X_explain)

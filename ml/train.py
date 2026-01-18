# ml/train.py

import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from xgboost import XGBRegressor

from preprocess import preprocess_data  # script-style import

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "../data/LengthOfStay.csv")
MODEL_PATH = os.path.join(BASE_DIR, "los_regression_model.pkl")

# -------------------------------------------------
# Load & preprocess (save feature order)
# -------------------------------------------------
X, y = preprocess_data(DATA_PATH, save_features=True)

# -------------------------------------------------
# Split
# -------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------------------------
# Model
# -------------------------------------------------
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

# -------------------------------------------------
# Train
# -------------------------------------------------
model.fit(X_train, y_train)

# -------------------------------------------------
# Evaluate
# -------------------------------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("✅ Model trained successfully")
print(f"MAE  : {mae:.2f} days")
print(f"RMSE : {rmse:.2f} days")

# -------------------------------------------------
# Save model
# -------------------------------------------------
joblib.dump(model, MODEL_PATH)
print("✅ Model saved at:", MODEL_PATH)

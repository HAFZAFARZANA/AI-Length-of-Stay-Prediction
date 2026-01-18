import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

from preprocess import preprocess_data

# Load data
X, y, _ = preprocess_data("../data/LengthOfStay.csv")

# Train-test split (same as training)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("los_regression_model.pkl")

# Predict
y_pred = model.predict(X_test)

# Plot: Actual vs Predicted
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)
plt.xlabel("Actual Length of Stay (days)")
plt.ylabel("Predicted Length of Stay (days)")
plt.title("Actual vs Predicted Length of Stay")
plt.show()

from ml.user_input_handler import build_patient_record
from ml.predict import predict_length_of_stay
from ml.patient_shap_explain import explain_single_patient
from ml.llm_explanation import generate_llm_explanation

# Rounded prediction (from your predict.py output)
predicted_days = 12

# Same patient input you used
sample_patient = {
    "rcount": 2,
    "gender": "M",
    "dialysisrenalendstage": 0,
    "asthma": 1,
    "irondef": 0,
    "pneum": 0,
    "substancedependence": 0,
    "psychologicaldisordermajor": 1,
    "depress": 0,
    "psychother": 0,
    "fibrosisandother": 0,
    "malnutrition": 0,
    "hemo": 0,
    "hematocrit": 38,
    "neutrophils": 60,
    "sodium": 138,
    "glucose": 110,
    "bloodureanitro": 20,
    "creatinine": 1.4,
    "bmi": 26,
    "pulse": 92,
    "respiration": 20,
    "secondarydiagnosisnonicd9": 1,
    "discharged": 0,
    "facid": 3
}

# Get SHAP explanation
shap_df = explain_single_patient(sample_patient).head(6)

# Generate LLM explanation
llm_output = generate_llm_explanation(predicted_days, shap_df)

print("\n🩺 LLM Explanation:\n")
print(llm_output)

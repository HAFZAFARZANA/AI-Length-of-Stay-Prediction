from ml.patient_shap_explain import explain_single_patient
from ml.llm_explanation import generate_llm_explanation

def explanation_agent(patient_data, predicted_los):
    shap_df = explain_single_patient(patient_data)
    return generate_llm_explanation(predicted_los, shap_df)

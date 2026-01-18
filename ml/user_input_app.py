# ml/user_input_app.py


from ml.user_input_handler import build_patient_record
from ml.predict import predict_length_of_stay
from ml.patient_shap_explain import explain_single_patient
from ml.llm_explanation import generate_llm_explanation

def safe_input(prompt, cast, min_val, max_val):
    while True:
        try:
            value = cast(input(prompt))
            if value < min_val or value > max_val:
                raise ValueError
            return value
        except ValueError:
            print(f"⚠️ Enter a value between {min_val} and {max_val}")

def get_user_input():
    print("\nEnter patient details (realistic clinical ranges):\n")

    return {
        "rcount": safe_input("Prior admissions count (0–10): ", int, 0, 10),
        "gender": input("Gender (M/F): ").upper(),
        "respiration": safe_input("Respiration rate (12–30): ", float, 12, 30),
        "pulse": safe_input("Pulse rate (50–140): ", int, 50, 140),
        "bmi": safe_input("BMI (15–45): ", float, 15, 45),
        "creatinine": safe_input("Creatinine (0.5–3.5): ", float, 0.5, 3.5),
        "neutrophils": safe_input("Neutrophils % (30–80): ", float, 30, 80),
    }

if __name__ == "__main__":
    user_input = get_user_input()

    patient = build_patient_record(user_input)

    predicted_los = predict_length_of_stay(patient)
    print(f"\n🧮 Predicted Length of Stay: {predicted_los}")

    shap_df = explain_single_patient(patient).head(6)

    explanation = generate_llm_explanation(predicted_los, shap_df)
    print("\n🩺 Explanation:\n")
    print(explanation)

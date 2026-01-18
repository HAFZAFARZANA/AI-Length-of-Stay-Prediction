from fastapi import FastAPI
from pydantic import BaseModel
from ml.user_input_handler import build_patient_record
from ml.predict import predict_length_of_stay
from ml.patient_shap_explain import explain_single_patient
from ml.llm_explanation import generate_llm_explanation
from fastapi.middleware.cors import CORSMiddleware

# ✅ FastAPI instance (THIS IS REQUIRED)
app = FastAPI(
    title="Patient LOS Prediction API",
    version="1.0"
)

# ✅ Allow frontend (React) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Request schema
# ----------------------------
class PatientInput(BaseModel):
    rcount: int
    gender: str
    respiration: float
    pulse: int
    bmi: float
    creatinine: float
    neutrophils: float

# ----------------------------
# Health check
# ----------------------------
@app.get("/")
def root():
    return {"status": "LOS API running"}

# ----------------------------
# Prediction endpoint
# ----------------------------
@app.post("/predict")
def predict_los(data: PatientInput):
    user_data = data.dict()

    patient = build_patient_record(user_data)

    predicted_los = predict_length_of_stay(patient)

    shap_df = explain_single_patient(patient).head(3)

    explanation = generate_llm_explanation(predicted_los, shap_df)

    return {
        "los": predicted_los,
        "explanation": explanation
    }

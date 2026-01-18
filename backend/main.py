from fastapi import FastAPI
from backend.schemas import PatientInput, PredictionResponse
from ml.user_input_handler import build_patient_record
from agents.los_agent import los_agent

app = FastAPI(title="Patient LOS Prediction API")

@app.post("/predict", response_model=PredictionResponse)
def predict_los(data: PatientInput):
    patient = build_patient_record(data.dict())
    los, explanation = los_agent(patient)

    return {
        "predicted_los": los,
        "explanation": explanation
    }

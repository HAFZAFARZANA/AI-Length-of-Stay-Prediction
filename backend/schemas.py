from pydantic import BaseModel

class PatientInput(BaseModel):
    rcount: int
    gender: str
    respiration: float
    pulse: int
    bmi: float
    creatinine: float
    neutrophils: float

class PredictionResponse(BaseModel):
    predicted_los: str
    explanation: str

# ml/user_input_handler.py

# Default (assumed) values for features user does NOT enter
DEFAULT_VALUES = {
    "dialysisrenalendstage": 0,
    "asthma": 0,
    "irondef": 0,
    "pneum": 0,
    "substancedependence": 0,
    "psychologicaldisordermajor": 0,
    "depress": 0,
    "psychother": 0,
    "fibrosisandother": 0,
    "malnutrition": 0,
    "hemo": 0,
    "hematocrit": 40,
    "sodium": 138,
    "glucose": 105,
    "bloodureanitro": 18,
    "secondarydiagnosisnonicd9": 0,
    "discharged": 0,
    "facid": 1
}

# Fields the USER MUST enter
REQUIRED_FIELDS = [
    "rcount",
    "gender",
    "respiration",
    "pulse",
    "bmi",
    "creatinine",
    "neutrophils"
]

def build_patient_record(user_input: dict):
    """
    Builds a full patient record using:
    - User provided high-impact fields
    - Default values for remaining fields
    """

    patient = {}

    # Validate required fields
    for field in REQUIRED_FIELDS:
        if field not in user_input:
            raise ValueError(f"Missing required field: {field}")
        patient[field] = user_input[field]

    # Fill remaining fields with defaults
    for key, value in DEFAULT_VALUES.items():
        patient[key] = value

    return patient

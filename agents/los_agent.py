# agents/los_agent.py

from agents.data_agent import data_agent
from agents.prediction_agent import prediction_agent
from agents.explanation_agent import explanation_agent

def los_agent(user_input):
    patient = data_agent(user_input)
    los = prediction_agent(patient)
    explanation = explanation_agent(patient, los)

    return los, explanation

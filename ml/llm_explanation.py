# ml/llm_explanation.py

from groq import Groq
from rag.retrieve import retrieve_context

client = Groq(
    api_key="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"
)

FEATURE_DESCRIPTIONS = {
    "rcount": "multiple prior hospital admissions",
    "creatinine": "renal dysfunction",
    "respiration": "respiratory instability",
    "pulse": "cardiovascular stress",
    "bmi": "abnormal body mass index",
    "neutrophils": "inflammatory response",
    "hematocrit": "possible anemia"
}

def generate_llm_explanation(predicted_los, shap_df):
    top_features = shap_df.head(2)

    factors_text = ", ".join(
        FEATURE_DESCRIPTIONS.get(row.feature, row.feature)
        for _, row in top_features.iterrows()
    )

    rag_query = f"hospital length of stay due to {factors_text}"
    rag_context = retrieve_context(rag_query, top_k=1)

    prompt = f"""
You are a clinical decision support assistant.

STRICT RULES:
- Output EXACTLY this structure
- 5 bullet points per section
- Short clinical phrases
- No extra text

FORMAT:

CLINICAL_SUMMARY:
- ...
- ...
- ...
- ...
- ...

RECOMMENDATION:
- ...
- ...
- ...
- ...
- ...

Predicted LOS: {predicted_los}

Patient factors:
{factors_text}

Evidence:
{rag_context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You generate structured clinical summaries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=120
    )

    return response.choices[0].message.content.strip()

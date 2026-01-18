# rag/retrieve.py

import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "rag_index.pkl")

def retrieve_context(query, top_k=2):
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError(f"RAG index not found at {INDEX_PATH}")

    vectorizer, doc_vectors, documents = joblib.load(INDEX_PATH)

    # Transform query
    query_vec = vectorizer.transform([query])

    # 🔑 FIX: convert sparse result to numpy array
    similarity_scores = (doc_vectors @ query_vec.T).toarray().ravel()

    # Get top-k documents
    top_indices = similarity_scores.argsort()[-top_k:][::-1]

    return "\n\n".join(documents[i] for i in top_indices)

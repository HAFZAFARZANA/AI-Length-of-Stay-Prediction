# rag/build_index.py

import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = os.path.dirname(__file__)
DOCS_DIR = os.path.join(BASE_DIR, "docs")
INDEX_PATH = os.path.join(BASE_DIR, "rag_index.pkl")

def build_index():
    documents = []

    # Load ALL .txt files inside rag/docs
    for file in os.listdir(DOCS_DIR):
        if file.endswith(".txt"):
            file_path = os.path.join(DOCS_DIR, file)
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

    if not documents:
        raise ValueError("❌ No .txt documents found in rag/docs")

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    with open(INDEX_PATH, "wb") as f:
        pickle.dump((vectorizer, vectors, documents), f)

    print("✅ RAG index built successfully with", len(documents), "documents")

if __name__ == "__main__":
    build_index()

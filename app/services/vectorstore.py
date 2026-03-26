from langchain_community.vectorstores import FAISS
from app.services.embedding import get_embedding
import os

DB_PATH = "faiss_index"

def load_vectorstore():
    embeddings = get_embedding()

    if not os.path.exists(DB_PATH):
        raise ValueError(
            "Vectorstore not found. Run ingestion script first."
        )

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

def save_vectorstore(vectorstore):
    vectorstore.save_local(DB_PATH)
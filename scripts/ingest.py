from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.services.embedding import get_embedding
from app.services.vectorstore import save_vectorstore

def ingest():

    loader1 = PyPDFLoader("data/Designing Data Intensive Applications by Martin Kleppmann.pdf")
    loader2 = PyPDFLoader("data/System Design Interview by Alex Xu.pdf")

    docs1 = loader1.load()
    docs2 = loader2.load()
    docs = docs1 + docs2

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)
    embeddings = get_embedding()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    save_vectorstore(vectorstore)


if __name__ == "__main__":
    ingest()
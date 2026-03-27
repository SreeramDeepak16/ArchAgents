from app.services.vectorstore import load_vectorstore
from app.graph.state import ModelerState

def rag_node(state: ModelerState) -> ModelerState:
    vectorstore = load_vectorstore()

    if vectorstore is None:
        return {"documents": []}
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    print("Performing RAG...")

    query = state.rag_query

    docs = retriever.invoke(query)

    documents = [doc.page_content for doc in docs]

    return {
        "documents": documents
    }
from app.services.vectorstore import load_vectorstore
from app.graph.state import ModelerState

def rag_node(state: ModelerState) -> ModelerState:
    vectorstore = load_vectorstore()

    if vectorstore is None:
        return {"documents": []}
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    analyst_state = state.analyst_state

    print("Performing RAG...")

    query = f"""
    Functional requirements - 
    {analyst_state.fr}

    Non-functional requirements - 
    {analyst_state.nfr}

    Architecturally significant requirements - 
    {analyst_state.asr}

    Design constraints - 
    {analyst_state.dc}

    Retrieve relevant UML patterns, architecture styles and design mappings
    for the above given system.
    """

    docs = retriever.invoke(query)

    documents = [doc.page_content for doc in docs]

    return {
        "documents": documents
    }
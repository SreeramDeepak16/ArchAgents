from app.nodes.rag_query import generate_rag_query
from app.nodes.rag import rag_node
from app.nodes.generate_uml import generate_uml
from app.graph.state import ModelerState
from langgraph.graph import StateGraph, START, END

def build_modeler_graph():

    graph = StateGraph(ModelerState)

    graph.add_node("generate_rag_query", generate_rag_query)
    graph.add_node("rag", rag_node)
    graph.add_node("generate_uml", generate_uml)

    graph.add_edge(START, "generate_rag_query")
    graph.add_edge("generate_rag_query", "rag")
    graph.add_edge("rag", "generate_uml")
    graph.add_edge("generate_uml", END)

    return graph.compile()

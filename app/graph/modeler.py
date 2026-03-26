from app.nodes.rag import rag_node
from app.nodes.generate_uml import generate_uml
from app.graph.state import ModelerState
from langgraph.graph import StateGraph, START, END

def build_modeler_graph():

    graph = StateGraph(ModelerState)

    graph.add_node("rag", rag_node)
    graph.add_node("generate_uml", generate_uml)

    graph.add_edge(START, "rag")
    graph.add_edge("rag", "generate_uml")
    graph.add_edge("generate_uml", END)

    return graph.compile()

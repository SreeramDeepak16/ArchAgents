from langgraph.graph import StateGraph, START, END
from app.graph.state import AnalystState
from app.nodes.extract_requirements import get_req

def build_analyst_graph():

    graph = StateGraph(AnalystState)

    graph.add_node("get_requirements", get_req)

    graph.add_edge(START, "get_requirements")
    graph.add_edge("get_requirements", END)

    return graph.compile()

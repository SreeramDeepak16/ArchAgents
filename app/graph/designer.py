from langgraph.graph import START,END,StateGraph
from app.graph.state import DesignerState
from app.nodes.getLowLevelDesign import getLowLevelDesign

def build_designer_graph():
    graph=StateGraph(DesignerState)

    graph.add_node("getLowLevelDesign",getLowLevelDesign)

    graph.add_edge(START,"getLowLevelDesign")
    graph.add_edge("getLowLevelDesign",END)

    return graph.compile()
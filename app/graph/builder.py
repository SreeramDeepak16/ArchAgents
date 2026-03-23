from langgraph.graph import StateGraph, START, END
from app.graph.state import ArchState
from app.nodes.srs_generator import generate_srs
from app.graph.analyst import build_analyst_graph


def analyst_agent(state: ArchState):

    agent = build_analyst_graph()
    analyst_state = agent.invoke({'srs': state.srs})
    return {
        'analyst_state': analyst_state
    }


def build_graph():

    graph = StateGraph(ArchState)

    graph.add_node("generate_srs", generate_srs)
    graph.add_node("analyst_agent", analyst_agent)

    graph.add_edge(START, "generate_srs")
    graph.add_edge("generate_srs", "analyst_agent")
    graph.add_edge("analyst_agent", END)

    return graph.compile()
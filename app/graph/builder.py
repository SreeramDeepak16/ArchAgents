from langgraph.graph import StateGraph, START, END
from app.graph.state import ArchState
from app.nodes.srs_generator import generate_srs
from app.graph.analyst import build_analyst_graph
from app.graph.modeler import build_modeler_graph
from app.graph.designer import build_designer_graph

def analyst_agent(state: ArchState):

    agent = build_analyst_graph()
    analyst_state = agent.invoke({'srs': state.srs})
    return {
        'analyst_state': analyst_state
    }


async def modeler_agent(state: ArchState):
    
    agent = build_modeler_graph()
    modeler_state = await agent.ainvoke({'analyst_state': state.analyst_state})
    return {
        'modeler_state': modeler_state
    }

def designer_agent(state: ArchState):

    agent = build_designer_graph()

    designer_state = agent.invoke({
        "analyst_state": state.analyst_state,
        "modeler_state": state.modeler_state
    })

    return {
        "designer_state": designer_state
    }

def build_graph():

    graph = StateGraph(ArchState)

    graph.add_node("generate_srs", generate_srs)
    graph.add_node("analyst_agent", analyst_agent)
    graph.add_node("modeler_agent", modeler_agent)
    graph.add_node("designer_agent",designer_agent)

    graph.add_edge(START, "generate_srs")
    graph.add_edge("generate_srs", "analyst_agent")
    graph.add_edge("analyst_agent", "modeler_agent")
    graph.add_edge("modeler_agent","designer_agent")
    graph.add_edge("designer_agent",END)

    return graph.compile()
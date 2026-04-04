from dotenv import load_dotenv
load_dotenv()

from app.graph.builder import build_graph

def get_arch(description: str):

    graph = build_graph()
    result = graph.invoke(
    {'description': description},
    config={"configurable": {"thread_id": "1"}}
)

    modeler_state = result['modeler_state']

    for (t,c) in zip(modeler_state['diagram_types'], modeler_state['diagram_codes']):
        print(t)
        print(c)
        print("\n\n\n")


description = '''Social media platform focused on sharing visual content such as photos and videos.'''

get_arch(description)
from app.graph.builder import build_graph
import asyncio

async def get_arch(description: str):

    graph = build_graph()
    result = await graph.ainvoke({'description': description})
    modeler_state = result['modeler_state']
    for (t,c) in zip(modeler_state['diagram_types'], modeler_state['diagram_codes']):
        print(t)
        print(c)
        print("\n\n\n")

description = '''Social media platform focused on sharing visual content such as photos and videos.'''

if __name__ == "__main__":
    asyncio.run(get_arch(description))
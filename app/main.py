from app.graph.builder import build_graph

def get_arch(description: str):

    graph = build_graph()
    result = graph.invoke({'description': description})

    fr = result['analyst_state']['fr']
    nfr = result['analyst_state']['nfr']
    asr = result['analyst_state']['asr']
    dc = result['analyst_state']['dc']
    print(fr)
    print(nfr)
    print(asr)
    print(dc)
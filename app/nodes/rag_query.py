from app.services.llm import get_llm
from app.graph.state import ModelerState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = get_llm()

prompt_file_path = "app/prompts/rag_query_generator.txt"

def generate_rag_query(state: ModelerState) -> ModelerState:

    try:
        with open(prompt_file_path, 'r', encoding='utf8') as file:
            RAG_QUERY_GENERATOR_PROMPT = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{prompt_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    prompt = PromptTemplate(
        template=RAG_QUERY_GENERATOR_PROMPT,
        input_variables=['fr','nfr','asr','dc']
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    analyst_state = state.analyst_state
    fr = analyst_state.fr
    nfr = analyst_state.nfr
    asr = analyst_state.asr
    dc = analyst_state.dc

    query = chain.invoke({'fr': fr, 'nfr': nfr, 'asr': asr, 'dc': dc})

    return {
        'rag_query': query
    }


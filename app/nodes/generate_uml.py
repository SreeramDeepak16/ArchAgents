from app.graph.state import ModelerState
from app.services.llm import get_llm
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
import asyncio

llm = get_llm()

prompt_file_path = "app/prompts/uml_generator.txt"

UML_TYPES = [
    "Component diagram",
    "Package diagram",
    "Class diagram",
    "Object diagram",
    "State diagram",
    "Container diagram",
    "Deployment diagram",
    "Activity diagram",
    "Collaboration diagram",
    "Sequence diagram",
    "Use case diagram"
]

async def generate_uml(state: ModelerState) -> ModelerState:

    try:
        with open(prompt_file_path, 'r', encoding='utf8') as file:
            UML_GENERATOR_PROMPT = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{prompt_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Generating UML codes...")

    analyst_state = state.analyst_state
    fr = analyst_state.fr
    nfr = analyst_state.nfr
    asr = analyst_state.asr
    dc = analyst_state.dc
    documents = state.documents

    prompt = PromptTemplate(
        template=UML_GENERATOR_PROMPT,
        input_variables=['diagram', 'fr', 'nfr', 'asr', 'dc', 'documents']
    )
    parser = StrOutputParser()
    chain = prompt | llm | parser
    tasks = [
        chain.ainvoke({
            'diagram': uml,
            'fr': fr,
            'nfr': nfr,
            'asr': asr,
            'dc': dc,
            'documents': documents
        })
        for uml in UML_TYPES
    ]
    results = await asyncio.gather(*tasks)
    
    return {
        "diagram_types": UML_TYPES,
        "diagram_codes": [r.replace("\n"," ") for r in results]
    }



from app.services.llm import get_llm
from app.graph.state import AnalystState
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List

llm = get_llm()

class Requirements(BaseModel):
    fr: List[str] = Field(description="Functional requirements")
    nfr: List[str] = Field(description="Non-functional requirements")
    asr: List[str] = Field(description="Architecturally significant requirements")
    dc: List[str] = Field(description="Design constraints")

prompt_file_path = "app/prompts/analyst_agent.txt"

def get_req(state: AnalystState) -> AnalystState:

    try:
        with open(prompt_file_path, 'r', encoding='utf8') as file:
            ANALYST_AGENT_PROMPT = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{prompt_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    prompt = PromptTemplate(
        template=ANALYST_AGENT_PROMPT,
        input_variables=['srs']
    )

    structured_llm = llm.with_structured_output(Requirements)

    chain = prompt | structured_llm

    result = chain.invoke({'srs': state.srs})

    return {
        'fr': result.fr,
        'nfr': result.nfr,
        'asr': result.asr,
        'dc': result.dc
    }


    
from app.graph.state import ModelerState
from app.services.llm import get_llm
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

llm = get_llm()

prompt_file_path = "app/prompts/uml_generator.txt"

UML_TYPES = [
    "Use case diagram",
    "Activity diagram",
    "Sequence diagram",
    "Class diagram",
    "State diagram"
]

class UML(BaseModel):
    use_case_code: str = Field(description="Use case diagram code")
    activity_code: str = Field(description="Activity diagram code")
    sequence_code: str = Field(description="Sequence diagram code")
    class_code: str = Field(description="Class diagram code")
    state_code: str = Field(description="State diagram code")

def generate_uml(state: ModelerState) -> ModelerState:

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
    #documents = state.documents

    prompt = PromptTemplate(
        template=UML_GENERATOR_PROMPT,
        input_variables=['UML_TYPES', 'fr', 'nfr', 'asr', 'dc']
    )
    structured_llm = llm.with_structured_output(UML)
    chain = prompt | structured_llm
    result = chain.invoke({
        'UML_TYPES': UML_TYPES,
        'fr': fr,
        'nfr': nfr,
        'asr': asr,
        'dc': dc
    })
    results = [
        result.use_case_code,
        result.activity_code,
        result.sequence_code,
        result.class_code,
        result.state_code
    ]
    
    return {
        "diagram_types": UML_TYPES,
        "diagram_codes": results
    }



from app.services.llm import get_llm
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Optional
from app.graph.state import DesignerState

llm = get_llm()


class DesignerOutput(BaseModel):
    goals: Optional[str] = Field(description="What the system can achieve")
    architecture_design: Optional[str] = Field(description="Detailed architecture design")
    component_specs: Optional[str] = Field(description="Component & connector specifications")
    key_technologies: Optional[str] = Field(description="The technology stack used")
    design_decisions: Optional[str] = Field(description="Architectural patterns and decisions")
    design_rationale: Optional[str] = Field(description="Reasoning behind decisions")
    code_skeleton: Optional[str] = Field(description="High-level code skeleton / scaffolding")

prompt_file_path = "app/prompts/lowLevelDesign.txt"

def getLowLevelDesign(state: DesignerState):

    try:
        with open(prompt_file_path, 'r', encoding='utf8') as file:
            prompt = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{prompt_file_path}' was not found.")
        return DesignerOutput()
    except Exception as e:
        print(f"An error occurred: {e}")
        return DesignerOutput()

    analyst_state = state.analyst_state
    functional_requirements = analyst_state.fr
    non_functional_requirements = analyst_state.nfr
    architecturally_significant_requirements = analyst_state.asr
    design_constraints = analyst_state.dc

    modeler_state = state.modeler_state
    diagram_codes = modeler_state.diagram_codes
    documents = modeler_state.documents

    prompt = PromptTemplate(
        template=prompt,
        input_variables=[
            'functionalrequirements',
            'non_functionalrequirements',
            'architecturally_significant_requirements',
            'design_constraints',
            'diagram_codes',
            'documents'
        ]
    )

    
    structured_llm = llm.with_structured_output(DesignerOutput)

   
    chain = prompt | structured_llm

   
    result = chain.invoke({
        'functional_requirements': functional_requirements,
        'non_functional_requirements': non_functional_requirements,
        'architecturally_significant_requirements': architecturally_significant_requirements,
        'design_constraints': design_constraints,
        'diagram_codes': diagram_codes,
        'documents': documents
    })

    if result is None:
        return {}

    return {
        "goals": result.goals,
        "architecture_design": result.architecture_design,
        "component_specs": result.component_specs,
        "key_technologies": result.key_technologies,
        "design_decisions": result.design_decisions,
        "design_rationale": result.design_rationale,
        "code_skeleton": result.code_skeleton
    }

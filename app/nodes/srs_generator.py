from app.services.llm import get_llm
from app.graph.state import ArchState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_file_path = "app/prompts/srs_generator.txt"

llm = get_llm()

SRS_GENERATOR_PROMPT = ""

def generate_srs(state: ArchState) -> ArchState:
    
    try:
        with open(prompt_file_path, 'r', encoding='utf8') as file:
            SRS_GENERATOR_PROMPT = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{prompt_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Generating SRS...")

    prompt = PromptTemplate(
        template=SRS_GENERATOR_PROMPT,
        input_variables=['description']
    )

    parser = StrOutputParser()
    chain = prompt | llm | parser

    srs = chain.invoke({'description': state.description})

    return {
        'srs': srs
    }

    
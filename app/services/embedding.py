from langchain_mistralai import MistralAIEmbeddings
from app.utils.config import embedding_settings

def get_embedding():
    return MistralAIEmbeddings(
        model=embedding_settings.MODEL_NAME,
        api_key=embedding_settings.MISTRAL_API_KEY
    )
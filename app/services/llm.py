from langchain_mistralai import ChatMistralAI
from app.utils.config import settings

def get_llm():
    return ChatMistralAI(
        model=settings.MODEL_NAME,
        api_key=settings.MISTRAL_API_KEY,
        temperature=settings.TEMPERATURE,
        rate_limiter=settings.RATE_LIMITER
    )
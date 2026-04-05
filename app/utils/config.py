import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = "mistral-large-2411"
    TEMPERATURE = 0.2

settings = Settings()
class EmbeddingSettings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = "mistral-embed"


embedding_settings = EmbeddingSettings()
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = "ministral-8b-latest"
    TEMPERATURE = 0.2

settings = Settings()
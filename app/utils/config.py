import os
from dotenv import load_dotenv
from langchain_core.rate_limiters import InMemoryRateLimiter

load_dotenv()

rate_limiter = InMemoryRateLimiter(
    requests_per_second=1.0,
    check_every_n_seconds=0.1,
    max_bucket_size=1
)

class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = "mistral-large-2512"
    TEMPERATURE = 0.2
    RATE_LIMITER = rate_limiter

settings = Settings()

class EmbeddingSettings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MODEL_NAME = "mistral-embed"

embedding_settings = EmbeddingSettings()
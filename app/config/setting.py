from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "production RAG Chatbot" 
    APP_VERSION: str = "1.0.0"
    APP_ENV: str
    DEBUG: bool
    HOST:str
    PORT:int

    GROQ_API_KEY: str
    GROQ_MODEL: str

    EMBEDDING_MODEL: str
    RERANKER_MODEL: str

    QDRANT_URL : str
    QDRANT_API_KEY : str =""
    QDRANT_COLLECTION : str

    REDIS_HOST: str 
    REDIS_PORT : str
    REDIS_PASSWORD: str =""
    REDIS_DB: int

    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    TOP_K: int
    FINAL_TOP_K: int
    SEARCH_TYPE: str

    MAX_FILE_SIZE: int
    UPLOAD_DIR: str

    LOGGING: str

    LANGCHAIN_TRACING_V2 : bool
    LANGCHAIN_API_KEY: str
    LANCHAIN_PROJECT: str
    LANGCHAIN_ENDPOINT: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache
def get_settings():
    return Settings()

settings = get_settings

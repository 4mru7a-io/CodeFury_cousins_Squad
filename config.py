import os
from dataclasses import dataclass

@dataclass
class Settings:
    data_path: str = os.getenv("MODEL_DATA_PATH", "data/models.xlsx")
    collection_name: str = os.getenv("VECTOR_COLLECTION", "modelproof_models")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    vector_dir: str = os.getenv("VECTOR_DIR", "storage/chroma")
    llm_base_url: str = os.getenv("LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "gemini-2.5-flash")

settings = Settings()

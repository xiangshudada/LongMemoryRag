from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    dashscope_api_key: str
    llm_model: str = "qwen-plus"
    embedding_model: str = "text-embedding-v4"
    memory_root_dir: str = "./memory"
    cache_dir: str = "./.cache"
    top_k: int = 5
    vector_weight: float = 0.6
    bm25_weight: float = 0.4

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()

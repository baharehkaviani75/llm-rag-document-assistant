from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Enterprise PDF RAG Assistant"
    app_version: str = "0.1.0"

    ollama_base_url: str = "http://localhost:11434"
    llm_model: str = "qwen2.5:3b"

    embedding_model: str = "BAAI/bge-base-en-v1.5"

    vector_db_path: str = "./vector_db"
    pdf_storage_path: str = "./data/pdfs"

    langchain_tracing_v2: bool = False
    langchain_api_key: str | None = None
    langchain_project: str = "enterprise-pdf-rag"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
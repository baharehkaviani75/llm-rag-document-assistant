from fastapi import FastAPI

from app.config import settings
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise PDF RAG Assistant"
)


app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "llm": settings.llm_model,
        "embedding_model": settings.embedding_model,
    }
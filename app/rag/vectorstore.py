from langchain_chroma import Chroma

from app.config import settings
from app.rag.embeddings import get_embeddings


def get_vector_store(
    collection_name: str = "enterprise_pdf_rag"
):
    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=settings.vector_db_path,
    )

    return vector_store


def add_documents(documents):
    vector_store = get_vector_store()

    vector_store.add_documents(documents)

    return vector_store
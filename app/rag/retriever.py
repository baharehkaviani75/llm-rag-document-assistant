from app.rag.vectorstore import get_vector_store


def get_retriever(k: int = 5):

    vector_store = get_vector_store()


    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k
        },
    )


    return retriever
from sentence_transformers import CrossEncoder


#MODEL_NAME = "BAAI/bge-reranker-base"
MODEL_NAME = "BAAI/bge-reranker-small"


class BGEReranker:

    def __init__(self):

        self.model = CrossEncoder(
            MODEL_NAME
        )

    def rerank(
        self,
        query,
        documents,
        top_k=5,
    ):

        pairs = [
            (
                query,
                document.page_content
            )
            for document in documents
        ]

        scores = self.model.predict(
            pairs
        )

        scored_documents = list(
            zip(documents, scores)
        )

        scored_documents.sort(
            key=lambda x: float(x[1]),
            reverse=True
        )

        return scored_documents[:top_k]


reranker = BGEReranker()
from langchain_huggingface import HuggingFaceEmbeddings


_embeddings = None


def get_embeddings():

    global _embeddings


    if _embeddings is None:

        print("Loading embedding model...")

        _embeddings = HuggingFaceEmbeddings(

            model_name="BAAI/bge-small-en-v1.5",

            model_kwargs={
                "device": "cpu"
            },

            encode_kwargs={
                "normalize_embeddings": True
            }

        )

    return _embeddings


#from langchain_huggingface import HuggingFaceEmbeddings

#from app.config import settings


#def get_embeddings():
#    return HuggingFaceEmbeddings(
#        model_name=settings.embedding_model,
#        model_kwargs={
#            "device": "cpu"
#        },
#        encode_kwargs={
#            "normalize_embeddings": True
#        }
#    )
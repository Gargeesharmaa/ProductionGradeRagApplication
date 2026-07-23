from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings

@lru_cache
def get_embedding_model()->HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        model_kwargs={
            "device": "cpu",
            "trust_remote_code":True
        },
        encode_kwargs={
            "normalize_embeddings":True,
        }
    )
embedding_model = get_embedding_model()
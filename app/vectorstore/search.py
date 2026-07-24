from typing import List

from langchain_core.documents import Document

from app.config import settings
from app.embeddings.embedding_model import embedding_model
from app.vectorstore.qdrant_client import qdrant_client


class VectorSearcher:
    """
    Performs semantic search in Qdrant.
    """

    def __init__(self):
        self.client = qdrant_client
        self.collection_name = settings.QDRANT_COLLECTION

    def similarity_search(
        self,
        query: str,
        top_k: int = settings.TOP_K,
    ) -> List[Document]:
        """
        Search for the most similar document chunks.
        """

        query_vector = embedding_model.embed_query(query)

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
        )

        documents = []

        for point in results.points:
            payload = point.payload

            documents.append(
                Document(
                    page_content=payload["content"],
                    metadata={
                        key: value
                        for key, value in payload.items()
                        if key != "content"
                    },
                )
            )

        return documents
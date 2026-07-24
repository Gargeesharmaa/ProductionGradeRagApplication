from uuid import uuid4

from langchain_core.documents import Document
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.config import settings
from app.embeddings.embedding_model import embedding_model
from app.vectorstore.qdrant_client import qdrant_client


class VectorIndexer:
    """
    Creates collections and stores document embeddings in Qdrant.
    """

    def __init__(self):
        self.client = qdrant_client
        self.collection_name = settings.QDRANT_COLLECTION

    def create_collection(self):
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]

        if self.collection_name not in collection_names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=len(embedding_model.embed_query("test")),
                    distance=Distance.COSINE,
                ),
            )

    def index_documents(self, documents: list[Document]):
        points = []

        for document in documents:
            texts=[doc.page_content for doc in document]
            vector = embedding_model.embed_query(texts)

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=vector,
                    payload={
                        "content": document.page_content,
                        **document.metadata,
                    },
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )
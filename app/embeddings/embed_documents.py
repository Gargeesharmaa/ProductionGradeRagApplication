from typing import List
from langchain_core.documents import Document
from app.embeddings.embedding_model import embedding_model

class DocumentEmbedder:
    """Generate embedding for document and user queries."""
    def __init__(self):
        self.embedding_model=embedding_model

    def embed_documents(self, documents: List[Document])-> List[List[float]]:
        """generate embeddings for document chunks."""
        texts = [doc.page_content for doc in documents]
        return self.embedding_model.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        """generate embedding for a user query."""
        return self.embedding_model.embed_query(query)
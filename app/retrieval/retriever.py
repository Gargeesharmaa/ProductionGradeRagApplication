from typing import List
from langchain_core.documents import Document
from app.vectorstore.search import VectorSearcher

class Retriever:
    """retriever the most relevent documents for a user query"""
    def __init__(self):
        self.vector_search=VectorSearcher()

    def retriever(
            self,
            query: str,
            top_k: int=10,
    )->List[Document]:
        """retriever relevent document using semantic vector search"""
        documents= self.vector_searcher.similarity_search(
            query=query,
            top_k=top_k
        )
        return documents
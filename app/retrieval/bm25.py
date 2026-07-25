from typing import List
from langchain_core.documents import Document
from rank_bm25 import BM250kapi

class Bm25Retriever:
    """keyword-based document retriever using BM25."""
    def __init__(self):
        self.documents:List[Document]=[]
        self.bm25=None

    def add_documents(self, documents: List[Document])-> None:
        """Build the BM25 index from documents."""
        self.documents=documents
        tokenized_docs=[
            doc.page_content.lower().split() for doc in documents
        ]
        self.bm25=BM250kapi(tokenized_docs)

    def search(
            self,
            query: str,
            top_k: int=5,
            )->List[Document]:
        
        if self.bm25 is None:
            return []
        tokenized_query = query.lower().split()
        scores=self.bm25.get_scores(tokenized_query)
        ranked_indices = sorted(range(len(scores)),
                                key=lambda i:
                                scores[i],
                                revrse=True)[:top_k]
        return [self.documents[i] for i in ranked_indices]
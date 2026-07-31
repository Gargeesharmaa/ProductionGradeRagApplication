from typing import Annotated, List
from langchain_core.documents import Document
from typing_extensions import TypedDict

class GraphState(TypedDict):
    """Shared state passed between langgraph nodes"""
    session_id: str
    question: str
    chat_history: str
    retrieved_documents:List[Document]
    context: str
    answer: str


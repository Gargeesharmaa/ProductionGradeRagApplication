from functools import lru_cache

from langchain_groq import ChatGroq

from app.config import settings
from ProductionGradeRagApplication.app.llm.groq_client import RAG_PROMPT


@lru_cache
def get_llm() -> ChatGroq:
    """
    Create a singleton Groq LLM instance.
    """
    return ChatGroq(
        model=settings.LLM_MODEL,
        api_key=settings.GROQ_API_KEY,
        temperature=0.0,
        max_tokens=1024,
    )


class GroqLLM:
    """
    Handles response generation using Groq.
    """

    def __init__(self):
        self.llm = get_llm()

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:

        prompt = RAG_PROMPT.invoke(
            {
                "question": question,
                "context": context,
            }
        )

        response = self.llm.invoke(prompt)

        return response.content
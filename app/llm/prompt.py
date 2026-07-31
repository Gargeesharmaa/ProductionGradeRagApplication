from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI assistant.

Answer ONLY using the provided context.

Rules:
1. Do not make up information.
2. If the answer is not in the context, reply:
   "I couldn't find the answer in the provided documents."
3. Keep answers concise and accurate.
4. Cite the source filename and page number whenever possible.
5. If multiple documents support the answer, mention all relevant sources.
            """,
        ),
        (
            "human",
            """
Question:
{question}

Context:
{context}

Answer:
            """,
        ),
    ]
)
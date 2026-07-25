from typing import List

from langchain_core.documents import Document


class ContextBuilder:
    """
    Builds formatted context for the LLM.
    """

    def build(
        self,
        documents: List[Document],
    ) -> str:

        if not documents:
            return "No relevant context found."

        context_parts = []

        for index, document in enumerate(documents, start=1):

            source = document.metadata.get("filename", "Unknown")
            page = document.metadata.get("page", "N/A")

            context_parts.append(
                f"""
Document {index}
Source: {source}
Page: {page}

Content:
{document.page_content}
"""
            )

        return "\n\n".join(context_parts)
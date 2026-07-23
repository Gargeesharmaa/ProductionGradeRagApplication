from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


class DocumentChunker:
    """
    Splits cleaned documents into smaller overlapping chunks.
    """

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],
        )

    def split_text(
        self,
        text: str,
        metadata: dict
    ) -> List[Document]:

        return self.text_splitter.create_documents(
            texts=[text],
            metadatas=[metadata]
        )
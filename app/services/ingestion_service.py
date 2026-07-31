from pathlib import Path

from app.embeddings.embed_documents import DocumentEmbedder
from app.ingestion.chunker import DocumentChunker
from app.ingestion.cleaner import TextCleaner
from app.ingestion.metadata import MetadataExtractor
from app.ingestion.parser import DocumentParser
from app.vectorstore.index import VectorIndexer


class IngestionService:

    def __init__(self):
        self.parser = DocumentParser()
        self.cleaner = TextCleaner()
        self.chunker = DocumentChunker()
        self.indexer = VectorIndexer()
        self.embedder = DocumentEmbedder()

    def ingest(self, file_path: str):

        raw_text = self.parser.parse(file_path)

        clean_text = self.cleaner.normalize_text(raw_text)

        metadata = MetadataExtractor.extract(file_path)

        documents = self.chunker.split_text(
            clean_text,
            metadata,
        )

        self.indexer.create_collection()

        self.indexer.index_documents(documents)

        return len(documents)
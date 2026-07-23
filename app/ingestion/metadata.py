from pathlib import Path
from typing import Dict
from uuid import uuid4
class MetadataExtractor:
    """Extract metadata for each document."""
    @staticmethod
    def extract (file_path: str, page: int| None=None)->Dict:
        path = Path(file_path)
        return {
            "document_id": str(uuid4()),
            "filename" : path.name,
            "source": str(path),
            "file_type": path.suffix.replace(".", "").lower(),
            "page": page
            }
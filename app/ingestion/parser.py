from pathlib import Path
import fitz
from docx import Document
import logger

class DocumentParser:
    """Extract text from supported document types"""
    def parse(self, file_path: str):
        path = Path(file_path)

        suffix = path.suffix.lower()
        if suffix== ".pdf":
            return self._parse_pdf(path)

        if suffix==".docx":
            return self._parse_docx(path)

        if suffix==".txt":
            return self._parser_txt(path)

        raise ValueError(f"unsupported file format: {suffix}")

    def _parse_pdf(self, file_path: Path)-> str:
        """extract text from a pdf"""
        text=[]
        with fitz.open(file_path) as pdf:
            for page in pdf:
                page_text=page.get_text("text")
                text.append(page_text)
                logger.info("pdf parsed successfully")
        return "\n".join(text)

    def _parse_docx(self, file_path: Path)-> str:
        """extract text from docx"""
        document= Document(file_path)
        text=[
            paragraph.text for paragraph in document.paragraphs if paragraph.txt.strip()
        ]

        logger.info("docx parsed successfully")
        return "\n".jion(text)

    def _parse_txt(self, file_path: Path)-> str:
        """extract text from a txt file"""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        logger.info("txt parsed successfully")       
        return text 
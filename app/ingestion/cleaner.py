import re

class TextCleaner:
    """Utility class for cleaning extracted document text."""
    @staticmethod
    def remove_extra_whitespace(text: str)-> str:
        """replace multiple space and tabs with a single space"""
        return re.sub(r"[ \t]+"," ",text)
    
    @staticmethod
    def remove_extra_newlines(text: str)->str:
        """replace multiple blank lines with a single blank line."""
        return re.sub(r"\n{2,}","\n\n", text)

    @staticmethod
    def remove_page_numbers(text: str):
        """remove common page number patterns.
        example :
        page 1
        page 25
        """
        return re.sub(r"(?im)^page\s+\d+\s*$", "", text)

    @staticmethod
    def normalize_text(text: str)->str:
        """run the complete cleaning pipeline."""
        text = text.strip()
        text = TextCleaner.remove_page_numbers(text)
        text = TextCleaner.remove_extra_whitespace(text)
        text = TextCleaner.remove_extra_newlines(text)
        return text.strip()

    
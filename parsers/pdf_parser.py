from PyPDF2 import PdfReader

from parsers.base import BaseParser
from utils.config import PDF_TEXT_LIMIT

class PDFParser(BaseParser):
    def __init__(self, limit=PDF_TEXT_LIMIT):
        super().__init__(file_types=['.pdf'], limit=limit)
    
    def load(self, path):
        self.assert_file_type(path)
        return PdfReader(path)
    
    def parse(self, path):
        pdf_obj = self.load(path)
        text = ''
        for page in pdf_obj.pages:
            text += page.extract_text()
            if len(text) > self._limit:
                break
        return text

        
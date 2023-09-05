from parsers.base import BaseParser
from PyPDF2 import PdfReader

class PDFParser(BaseParser):
    def __init__(self, limit=1000):
        super().__init__()
        self._file_types = ['pdf']
        self._limit = limit
    
    def load(self, path):
        assert path.suffix in self._file_types, 'File must be a pdf file'
        return PdfReader(path)
    
    def parse(self, path):
        pdf_obj = self.load(path)
        text = ''
        for page in pdf_obj.pages:
            text += page.extractText()
            if len(text) > self._limit:
                break
        return text

        
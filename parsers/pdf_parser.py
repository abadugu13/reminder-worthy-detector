from parsers.base import BaseParser
from PyPDF2 import PdfReader

class PDFParser(BaseParser):
    def __init__(self, limit=1000):
        super().__init__(file_types=['pdf'], limit=limit)
    
    def load(self, path):
        self.assert_file_type(path)
        return PdfReader(path)
    
    def parse(self, path):
        pdf_obj = self.load(path)
        text = ''
        for page in pdf_obj.pages:
            text += page.extractText()
            if len(text) > self._limit:
                break
        return text

        
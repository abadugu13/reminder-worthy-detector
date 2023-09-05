import pytesseract
from PIL import Image

from parsers.base import BaseParser

class ImageParser(BaseParser):
    def __init__(self, limit=1000):
        super().__init__(file_types=['.jpg', '.png'], limit=limit)
    
    def load(self, path):
        self.assert_file_type(path=path)
        return Image.open(path)

    def parse(self):
        image_obj = self.load()
        return pytesseract.image_to_string(image_obj)[:self.limit]
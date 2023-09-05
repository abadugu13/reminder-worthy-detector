import pytesseract
from PIL import Image

from parsers.base import BaseParser

class ImageParser(BaseParser):
    def __init__(self, limit=1000):
        super().__init__()
        self.limit = limit
        self._file_types = ['jpg', 'png', 'jpeg']
    
    def load(self):
        assert self.image_path.suffix in self._file_types, 'File must be an image'
        return Image.open(self.image_path)

    def parse(self):
        image_obj = self.load()
        return pytesseract.image_to_string(image_obj)[:self.limit]
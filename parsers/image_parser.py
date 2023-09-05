import pytesseract
from PIL import Image

from parsers.base import BaseParser
from utils.config import IMAGE_TEXT_LIMIT

class ImageParser(BaseParser):
    def __init__(self, limit=IMAGE_TEXT_LIMIT):
        super().__init__(file_types=['.jpg', '.png'], limit=limit)
    
    def load(self, path):
        self.assert_file_type(path=path)
        return Image.open(path)

    def parse(self, path):
        image_obj = self.load(path)
        return pytesseract.image_to_string(image_obj)[:self._limit]
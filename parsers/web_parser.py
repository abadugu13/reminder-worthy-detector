import requests
from bs4 import BeautifulSoup

from parsers.base import BaseParser
from utils.config import WEB_TEXT_LIMIT

class WebParser(BaseParser):
    def __init__(self, limit=WEB_TEXT_LIMIT):
        super().__init__(file_types=[], limit=limit)

    def load(self, url):
        response = requests.get(url)
        return response
    
    def parse(self, url):
        response = self.load(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(strip=True)
        return text[:self._limit]

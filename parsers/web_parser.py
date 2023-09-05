import requests
from bs4 import BeautifulSoup

from parsers.base import BaseParser


class WebParser(BaseParser):
    def __init__(self, limit=1000):
        super().__init__(file_types=[], limit=limit)

    def load(self, url):
        response = requests.get(url)
        return response
    
    def parse(self, url):
        response = self.load(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(strip=True)
        return text[:self.limit]

from abc import ABC, abstractmethod
import pathlib

from utils.timer import timer

class BaseParser(ABC):
    def __init__(self, file_types:list=None, limit:int=1000):
        self._file_types = file_types
        self._limit = limit
        
    def assert_file_type(self, path:pathlib.Path):
        if self._file_types:
            assert path.suffix in self._file_types, f'File must be one of the following types: {self._file_types}'
    @abstractmethod
    @timer
    def parse(self, path:pathlib.Path):
        pass

    def name(self):
        return self.__class__.__name__

    @abstractmethod
    def load(self, path:pathlib.Path):
        pass
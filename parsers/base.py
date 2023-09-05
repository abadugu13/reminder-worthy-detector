from abc import ABC, abstractmethod
import pathlib

from utils.timer import timer

class Parser(ABC):
    @abstractmethod
    @timer
    def parse(self, path:pathlib.Path):
        pass

    def name(self):
        return self.__class__.__name__

    @abstractmethod
    def load(self, path:pathlib.Path):
        pass
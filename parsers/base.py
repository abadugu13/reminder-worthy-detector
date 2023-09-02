from abc import ABC, abstractmethod
from utils.timer import timer

class Parser(ABC):
    @abstractmethod
    @timer
    def parse(self, data):
        pass

    def name(self):
        return self.__class__.__name__

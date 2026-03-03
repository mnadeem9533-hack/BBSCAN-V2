# scanners/base.py
from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan(self, engine, url, param):
        pass

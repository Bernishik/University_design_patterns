from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def getAuthor(self):
        pass
    @abstractmethod
    def isAvailable(self):
        pass
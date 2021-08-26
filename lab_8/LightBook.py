from Book import Book
from HeavyBook import HeavyBook

class LightBook(Book):
    def __init__(self):
        self.available = False
        self.heavyBook = HeavyBook()
        self.heavy = False
    def getName(self):
        if self.heavy:
            return self.heavyBook.getName()
        return "light name"

    def getAuthor(self):
        if self.heavy:
            return self.heavyBook.getAuthor()
        return "light author"
    def isAvailable(self):
        return  self.available

    def useHeavy(self):
        self.heavy = True
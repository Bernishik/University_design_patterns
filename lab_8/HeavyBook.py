from Book import Book


class HeavyBook(Book):
    def __init__(self):
        self.available = False
    def getName(self):
        return "heavy name"

    def getAuthor(self):
        return "heavy author"

    def isAvailable(self):
        return  self.available
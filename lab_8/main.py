from LightBook import LightBook

if __name__ == '__main__':
    book = LightBook()
    print(book.getAuthor())
    print(book.getName())
    book.useHeavy()
    print(book.getAuthor())
    print(book.getName())
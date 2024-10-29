# Aggregation = Represents a relationship where one or more object (the whole)
#              contains references to one or more INDEPENDENT objects (the parts)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("New york public library")

book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("To Kill a Mockingbird 1", "Harper Lee 1")
book3 = Book("To Kill a Mockingbird 2", "Harper Lee 2")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# print(library.list_books())
for book in library.list_books():
    print(book)


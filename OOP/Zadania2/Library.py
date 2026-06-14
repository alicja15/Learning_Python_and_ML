from Book import Book

class Library: 
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        self.__books.append(book)

    @property
    def available_books(self):
        return self.__books == False
    property
    def borrowed_count(self):
        counter = 0 
        for book in self.__books:
            if book.is_borrowed:
                counter += 1
        return counter
    


my_library = Library()

b1 = Book("Wiedźmin", "Sapkowski")
b2 = Book("Hobbit", "Tolkien")
b3 = Book("Rok 1984", "Orwell")

my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(b3)


b2.borrow()


print(f"Dostępne książki: {my_library.available_books}")
print(f"Liczba wypożyczonych: {my_library.borrowed_count}")

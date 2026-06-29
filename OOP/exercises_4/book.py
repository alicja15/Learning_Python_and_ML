class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
    
    def __str__(self):
        return (f"'{self.title}' by {self.author} ({self.year})")
    
    def __repr__(self):
        return (f"Book('{self.title}', '{self.author}', ({self.year})")

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False

#test objects
book1 = Book('Bolesław Prus', 'Lalka', 1890)
book2 = Book('Bolesław Prus', 'Lalka', 1890)
book3 = Book('Stanisław Wyspiański', 'Wesele', 1901)

print(book1 == book2) #True
print(book1 == book3) #False
print(repr(book1)) #Book('Lalka', 'Bolesław Prus', (1890)
print(book1) #'Lalka' by Bolesław Prus (1890

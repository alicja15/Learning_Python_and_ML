class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False

    @property
    def is_borrowed(self):
        return self.__is_borrowed
    
    def borrow(self):
        if self.__is_borrowed == False:
            self.__is_borrowed = True
            print(f"Borrowed '{self.title}'")
        else: 
            print("Already borrowed")
    def return_book(self):
        if self.__is_borrowed == True:
            self.__is_borrowed = False
            print(f"Returned '{self.title}'")
        else:
            print("Already returned")

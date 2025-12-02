class User: # klasa użytkownika
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.borowed_books = []
    
    def borow_book(self,book):
        if book.available:
            self.borowed_books.append(book)
            book.change_availability() #zmieniam status książki na niedostęoną
            print(f"{self.name} {self.surname} wypożyczył książkę {book.title}")
        else:
            print(f"książka {book.title} jest niedostępna do wypożyczenia.")

    def return_book(self,book):
        if book in self.borowed_books:
            self.borowed_books.remove(book)
            book.change_availability() # zmienny status książki
            print(f"{self.name} {self.surname} zwrócił książkę {book.title}")
        else:
            print(f"{self.name} {self.surname} nie wypożyczył  książki {book.title}")

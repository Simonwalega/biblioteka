from dekoratory import dekorator

class Library:
    def __init__(self):
        self.books = [] 
        self.users = [] 

    def add_book(self,book):
        self.books.append(book)

    def add_user (self, user):
        self.users.append(user)  

    def show_available_books(self):
        available_books = [book.title for book in self.books if book.available]
        print("Dostępne książki w bibliotece: ")
        for title in available_books:
            print(f" {title}")
    
    @dekorator.user_exists
    def show_borowed_books(self,user):
        borowed_books = [book.title for book in user.borowed_books]
        print(f"Wypożyczone książki przez {user.name} {user.surname}:")
        for title in borowed_books:
            print(f" {title}")
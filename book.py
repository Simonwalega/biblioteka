#klasa książki
class Book:
    def __init__(self, title, author, date_publication):
        self.title = title
        self.author = author
        self.date_publication = date_publication
        self.available = True

    def change_availability(self):
        self.available = not self.available
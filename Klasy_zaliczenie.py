from book import Book
from user import User
from library import Library
from dekoratory import dekorator


#przykładowe użycie
if __name__ == "__main__":
    # Tworzę obiekty, program
    library = Library()

    while True:
        print("\nBiblioteka - wybierz opcję:  ")
        print("1. Dodaj książkę")
        print("2. Dodaj użytkownika ")
        print("3. Pokaż dostępne książki")
        print("4. Wypożycz książkę")
        print("5. Zwróć książkę")
        print("6. Pokaż wypożyczone książki")
        print("7. Wyjście")

        choice = input("Wybierz opcję (1-7): \n")

        if choice == "1":
            title = input ("Podaj tytuł książki: ")  
            author = input("Podaj autora książki: ")
            date_publication = input("Podaj rok publikacji: ")
            library.add_book(Book(title,author,date_publication))
            print(f"Dodano książkę: {title}.")
        
        elif choice == "2":
            name = input("Podaj imie użytkownika: ")
            surname = input("Podaj nazwisko użytkownika: ")
            library.add_user(User(name,surname))
            print(f"Dodano użytkownika: {name} {surname}") 
        
        elif choice == "3":
           print(f" - {library.show_available_books()}")

        elif choice == "4":
            user_name = input("Podaj imię użytkownika: ")
            title = input("Podaj tytuł książki do wypożayczenia: ")
            
            user = next((u for u in library.users if u.name == user_name), None)
            book = next((b for b in library.books if b.title == title), None)


            if user and book:
                user.borow_book(book)
            else:
                print("Nie znaleziono użytkownika lub książki.")

        elif choice == "5":
            user_name = input("Podaj imię użytkownika: ") 
            title = input("Podaj tytuł książki do zwrotu: ")

            user = next((u for u in library.users if u.name == user_name), None)
            book = next((b for b in library.books if b.title == title), None)

            if user and book:
                user.return_book(book)
            else:
                print("Nie znaleziono użytkownika lub książki.")

        elif choice == "6":
            user_name = input("Podaj imię użytkownika: ")
            user = next((u for u in library.users if u.name == user_name), None)

            if user:
                library.show_borowed_books(user)
            else:
                print("Nie znaleziono użytkownika.")

        elif choice == "7":
            print("Zakończono program.")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")   
  
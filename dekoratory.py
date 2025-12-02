class dekorator:
    def user_exists(func):
        def wrapper(library, user_name, *args, **kwargs):
            user = next((u for u in library.users if u.name == user_name), None)
            if not user:
                print(f"Użytkownik {user_name} nie istnieje w bibliotece!")
                return None
            return func(library, user, *args, **kwargs)
        return wrapper
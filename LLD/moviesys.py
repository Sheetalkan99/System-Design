import uuid
from typing import Dict, Optional, List

class User:
    def __init__(self,name:str,email:str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
    def get_details(self):
        return f"User[{self.user_id}] - {self.name}"

class Movies:
    def __init__(self,title:str,genre: str,year:int):
        self.title = title
        self.genre = genre
        self.year = year
    
    def get_details(self):
        return f"{self.title} ({self.genre}, {self.year})"
        

class MovieDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieDB,cls).__new__(cls)
            cls._instance.users: Dict[str, User] = {}
            cls._instance.movies: Dict[str, dict] = {}
            cls._instance.borrowed_movies: Dict[str,dict] = {}

        return cls._instance
    
    
    @staticmethod
    def get_instance():
        if MovieDB._instance is None:
            MovieDB._instance = MovieDB()
        return MovieDB._instance



class ManageUser:
    def __init__(self):
        self.db = MovieDB.get_instance()
    
    def add_user(self,name:str,email:str):
        for user in self.db.users.values():
            if user.email == email:
                print("User with email already exists.")
                return user
        new_user = User(name,email)
        self.db.users[new_user.user_id] = new_user
        print(f"User {name} added succesfully.")
        return new_user
    
    def get_all_users(self):
        return list(self.db.users.values())

class ManageMovie:
    def __init__(self):
        self.db = MovieDB.get_instance()
    
    def add_movie(self,title:str,genre:str,year:int):
        if title in self.db.movies:
            print(f"Movie '{title}' already exists.")
            return self.db.movies[title]
        new_movie = Movies(title,genre,year)
        self.db.movies[new_movie.title] = new_movie
        print(f"Movie '{title}' added successfully.")
        return new_movie

    def get_all_movies(self):
        return list(self.db.movies.values())
    
class ManageRental:
    def __init__(self):
        self.db = MovieDB.get_instance()
    def borrowed_movie(self, user_id, movie_title):
        if user_id not in self.db.users:
            print("User not found")
            return
        if movie_title not in self.db.movies:
            print("Movie not found")
            return
        self.db.borrowed_movies.setdefault(user_id, [])
        if movie_title in self.db.borrowed_movies[user_id]:
            print(f"User already borrowed '{movie_title}'")
            return
        self.db.borrowed_movies[user_id].append(movie_title)
        print(f"'{movie_title}' borrowed by {self.db.users[user_id].name}.")
    def return_movie(self, user_id: str, movie_title: str):
        if user_id not in self.db.borrowed_movies or movie_title not in self.db.borrowed_movies[user_id]:
            print(f"{self.db.users[user_id].name} did not borrow '{movie_title}'.")
            return
        self.db.borrowed_movies[user_id].remove(movie_title)
        print(f"'{movie_title}' returned by {self.db.users[user_id].name}.")
    def display_borrowed(self, user_id: str):
        if user_id not in self.db.borrowed_movies or not self.db.borrowed_movies[user_id]:
            print(f"{self.db.users[user_id].name} has no borrowed movies.")
            return
        print(f"{self.db.users[user_id].name} has borrowed:")
        for title in self.db.borrowed_movies[user_id]:
            print(f"- {title}")

# ---------------------------
# Testing
# ---------------------------
if __name__ == "__main__":
    user_manager = ManageUser()
    movie_manager = ManageMovie()
    rental_manager = ManageRental()

    # Add Users
    u1 = user_manager.add_user("Alice", "alice@gmail.com")
    u2 = user_manager.add_user("Bob", "bob@gmail.com")
    user_manager.add_user("Alice Duplicate", "alice@gmail.com")  # duplicate

    # Add Movies
    m1 = movie_manager.add_movie("Inception", "Sci-Fi", 2010)
    m2 = movie_manager.add_movie("Interstellar", "Sci-Fi", 2014)
    movie_manager.add_movie("Inception", "Sci-Fi", 2010)  # duplicate

    # Borrow Movies
    rental_manager.borrowed_movie(u1.user_id, "Inception")
    rental_manager.borrowed_movie(u1.user_id, "Interstellar")
    rental_manager.borrowed_movie(u2.user_id, "Inception")
    rental_manager.borrowed_movie(u2.user_id, "Avatar")  # movie does not exist

    # Display borrowed movies
    print("\n--- Borrowed Movies ---")
    rental_manager.display_borrowed(u1.user_id)
    rental_manager.display_borrowed(u2.user_id)

    # Return Movies
    rental_manager.return_movie(u1.user_id, "Inception")
    rental_manager.return_movie(u2.user_id, "Inception")

    # Display after return
    print("\n--- After Returns ---")
    rental_manager.display_borrowed(u1.user_id)
    rental_manager.display_borrowed(u2.user_id)

    # Show all movies
    print("\n--- All Movies in DB ---")
    for movie in movie_manager.get_all_movies():
        print(movie.get_details())
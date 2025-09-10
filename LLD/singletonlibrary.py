from abc import ABC, abstractmethod
from typing import Dict

# ---------------------------
# User Classes
# ---------------------------
class User(ABC):
    def __init__(self, user_id: str, name: str) -> None:
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def get_details(self) -> str:
        pass


class Student(User):
    """Student only has ID and name; borrowed books stored centrally in LibraryDB"""
    def get_details(self) -> str:
        return f"Student ID: {self.user_id}, Name: {self.name}"

    def display_all_borrowed(self) -> None:
        db = LibraryDB.get_instance()
        borrowed = db.borrowed_books.get(self.user_id, {})
        if borrowed:
            print(f"{self.name} has borrowed:")
            for book_id, qty in borrowed.items():
                book = db.books.get(book_id)
                if book:
                    print(f"- {book.get_details_book()} (Qty: {qty})")
        else:
            print(f"{self.name} has no borrowed books.")


# ---------------------------
# Book Class
# ---------------------------
class Book:
    def __init__(self, book_id: str, title: str, author: str, copies: int = 1) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def get_details_book(self) -> str:
        return f"{self.title} by {self.author} (ID:{self.book_id})"


# ---------------------------
# LibraryDB Singleton
# ---------------------------
class LibraryDB:
    _instance: "LibraryDB" = None

    books: Dict[str, Book]
    students: Dict[str, Student]
    borrowed_books: Dict[str, Dict[str, int]]  # student_id -> {book_id -> qty}

    def __new__(cls) -> "LibraryDB":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = {}
            cls._instance.students = {}
            cls._instance.borrowed_books = {}
        return cls._instance

    @staticmethod
    def get_instance() -> "LibraryDB":
        if LibraryDB._instance is None:
            LibraryDB()
        return LibraryDB._instance


# ---------------------------
# Manager Class
# ---------------------------
class Manager(LibraryDB):
    def register_student(self, student: Student) -> None:
        self.students[student.user_id] = student

    def add_book(self, book: Book) -> None:
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
        else:
            self.books[book.book_id] = book

    def borrow_book(self, student_id: str, book_id: str) -> None:
        student = self.students.get(student_id)
        book = self.books.get(book_id)

        if not student:
            print("Student not found")
            return
        if not book:
            print("Book not found")
            return
        if book.copies <= 0:
            print(f"No copies left for '{book.title}'")
            return

        # Update central borrowed_books dictionary
        self.borrowed_books.setdefault(student_id, {})
        self.borrowed_books[student_id][book_id] = self.borrowed_books[student_id].get(book_id, 0) + 1
        book.copies -= 1
        print(f"{student.name} borrowed '{book.title}'")

    def return_book(self, student_id: str, book_id: str) -> None:
        student = self.students.get(student_id)
        book = self.books.get(book_id)

        if not student or not book:
            print("Invalid student or book")
            return
        if student_id not in self.borrowed_books or book_id not in self.borrowed_books[student_id]:
            print(f"{student.name} did not borrow '{book_id}'")
            return

        self.borrowed_books[student_id][book_id] -= 1
        book.copies += 1
        if self.borrowed_books[student_id][book_id] == 0:
            del self.borrowed_books[student_id][book_id]
        print(f"{student.name} returned '{book.title}'")


# ---------------------------
# Test Library System
# ---------------------------
if __name__ == "__main__":
    manager = Manager()

    # Register Students
    s1 = Student("S101", "Alice")
    s2 = Student("S102", "Bob")
    manager.register_student(s1)
    manager.register_student(s2)

    # Add Books
    b1 = Book("B001", "Python Basics", "John Doe", copies=2)
    b2 = Book("B002", "Data Structures", "Jane Smith", copies=1)
    manager.add_book(b1)
    manager.add_book(b2)

    # Borrow Books
    manager.borrow_book("S101", "B001")
    manager.borrow_book("S101", "B002")
    manager.borrow_book("S102", "B001")
    manager.borrow_book("S102", "B001")  # Should warn no copies left

    # Display borrowed books
    print("\n--- Borrowed Books ---")
    s1.display_all_borrowed()
    s2.display_all_borrowed()

    # Return Books
    manager.return_book("S101", "B001")
    manager.return_book("S102", "B001")

    # Display borrowed books after returning
    print("\n--- After Returning ---")
    s1.display_all_borrowed()
    s2.display_all_borrowed()

    # Remaining copies
    print("\n--- Remaining Copies ---")
    print(f"B001: {manager.books['B001'].copies}")
    print(f"B002: {manager.books['B002'].copies}")

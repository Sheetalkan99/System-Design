from Book import Book
from user import User
from Library import Library

# Initialize library
lib = Library()

# Create books
b1 = Book("Clean Code", "Robert C. Martin", "12345")
b2 = Book("The Pragmatic Programmer", "Andy Hunt", "23456")
b3 = Book("Introduction to Algorithms", "Cormen", "34567")

# Add books to library
lib.add_books(b1)
lib.add_books(b2)
lib.add_books(b3)

# List all books
lib.list_books()

# Create users
alice = User("Alice","11")
bob = User("Bob","22")

# Users borrow books
alice.borrow_book(b1)  # Success
bob.borrow_book(b1)    # Already borrowed

# Return book and try again
alice.return_book(b1)
bob.borrow_book(b1)    # Now it works

# Final list
lib.list_books()

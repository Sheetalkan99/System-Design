class book:
    def __init__(self,book_id,title,author,total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
class Library:
    def __init__(self):
        self.library = {}
        self.members = {}
    
    def add_book(self,book:book):
        if book.book_id in self.library:
            existing_book = self.library[book.book_id]
            existing_book.total_copies += book.total_copies
        else:
            self.library[book.book_id] = book

    def add_member(self,member:Member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
        else:
            print(f"Member Already Exists.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.library:
            member = self.members[member_id]
            book = self.library[book_id]
            if book.total_copies > 0:
                member.borrowed_books.append(book)
                book.total_copies -= 1
                print(f"{member.name} borrowed {book.title}")
            else:
                print(f"Book '{book.title}' is not available.")
        else:
            print("Invalid member ID or book ID")
  

    def return_book(self,member_id, book_id):
        if member_id in self.members and book_id in self.library:
            member = self.members[member_id]
            book = self.library[book_id]
            if book in member.borrowed_books:
                member.borrowed_books.remove(book)
                book.total_copies += 1
                print(f"{member.name} returned {book.title}")
            else:
                print(f"{member.name} has not borrowed {book.title}")
        else:
            print("Invalid member ID or book ID")
    def display_books(self):
        if not self.library:
            print("No books in the library.")
        else:
            for book in self.library.values():
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Copies: {book.total_copies}")


# ---------------- Example Usage ----------------
library = Library()

# Add books
library.add_book(book(101, "1984", "George Orwell", 3))
library.add_book(book(102, "The Hobbit", "J.R.R. Tolkien", 2))

# Add member
alice = Member(1, "Alice")
library.add_member(alice)

# Borrow and return
library.borrow_book(1, 101)
library.borrow_book(1, 102)
library.return_book(1, 101)

# Display
print(f"BOOKS IN SYSTEM:")
library.display_books()

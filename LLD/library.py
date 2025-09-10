from enum import Enum
class status(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"
    RESERVED = "reserved"


class Book:
    def __init__(self,title:str,author:str,ISBN:str,qty:int,status: status= status.AVAILABLE):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status
        self.qty = qty
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN:{self.ISBN}) - Status: {self.status.value}"

class Member:
    def __init__(self,name:str,memberID: int):
        self.name = name
        self.memberID = memberID
        self.borrowed = {}
    
    @classmethod
    def create_member(cls,name:str,memberID:int,member_type:str):
        if member_type.lower() == "student":
            return StudentMember(name,memberID)
        elif member_type.lower() == "faculty":
            return FacultyMember(name,memberID)
        else:
            raise ValueError("Invalid Member Type!")
    
    def __str__(self):
        borrowed_books = ', '.join([book.title for book in self.borrowed.values()])
        return f"Member: {self.name} (ID: {self.memberID}) - Borrowed Books: {borrowed_books if borrowed_books else 'None'}"

class StudentMember(Member):
    def __init__(self, name, memberID):
        super().__init__(name, memberID)
        self.borrow_limit = 3
class FacultyMember(Member):
    def __init__(self, name, memberID):
        super().__init__(name, memberID)
        self.borrow_limit = 5

class library:
    def __init__(self):
        self.books = {}
    
    def add_book(self,book:Book):
        if book.ISBN in self.books:
            self.books[book.ISBN].qty += book.qty
        else:
            self.books[book.ISBN] = book
    def borrow_book(self,book:Book,member:Member):
        if book.ISBN not in self.books:
            print(f"{book.title} is not availble in the library.")
            return

        if book.qty <= 0:
            print(f"{book.title} is currently out of stock.")

        if len(member.borrowed) >= member.borrow_limit:
            print(f"{member.name} cannot borrow more than {member.borrow_limit} books.")
            return 
        
        member.borrowed[book.ISBN] = book
        book.qty -= 1
        if book.qty == 0:
            book.status = status.BORROWED
        print(f"{member.name} borrowed {book.title}")

    def return_book(self,book:Book,member:Member):
        if book.ISBN in member.borrowed:
            del member.borrowed[book.ISBN] 
            book.qty += 1
            if book.qty > 0:
                book.status = status.AVAILABLE
            print(f"{member.name} returned {book.title}")
        else:
            print(f"{member.name} didn't borrowed this book.")
        



# Create the library
lib1 = library()

# Add some books
book1 = Book("Python 101", "Jane Doe", "1234", qty=2)
book2 = Book("Data Science Basics", "John Smith", "5678", qty=1)
lib1.add_book(book1)
lib1.add_book(book2)

# Create members
member1 = Member.create_member("Alice", 101, "student")   # borrow limit 3
member2 = Member.create_member("Bob", 102, "faculty")     # borrow limit 5

# Borrow books
lib1.borrow_book(book1, member1)  # Alice borrows Python 101
lib1.borrow_book(book2, member1)  # Alice borrows Data Science Basics
lib1.borrow_book(book1, member2)  # Bob borrows Python 101
lib1.return_book(book1, member2)
# Print current status
print("\nLibrary Books:")
for book in lib1.books.values():
    print(book)

print("\nMembers:")
print(member1)
print(member2)
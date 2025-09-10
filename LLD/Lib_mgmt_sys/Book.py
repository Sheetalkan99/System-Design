class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrower = None
        self.available = True

    def is_available(self):
        return self.available

    def borrow(self, user):
        if self.available:
            self.available = False
            self.borrower = user
            return True
        return False

    def return_book(self, user):
        if self.borrower == user:
            self.available = True
            self.borrower = None
            return True
        return False

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower.name}"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

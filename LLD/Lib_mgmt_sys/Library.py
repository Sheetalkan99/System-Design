class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to Library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                status = "Available" if book.is_available() else f"Borrowed by {book.borrower.name}"
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

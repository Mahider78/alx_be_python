class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for eBooks, extending Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the parent class constructor
        self.file_size = file_size  # File size in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for print books, extending Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the parent class constructor
        self.page_count = page_count  # Page count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class demonstrating composition."""
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        """Adds a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """Lists all books in the library."""
        for book in self.books:
            print(book)


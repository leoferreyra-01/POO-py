"""
Aggregation Relationship Documentation

Overview:
This module demonstrates the Aggregation relationship between Library and Book classes.
Aggregation is a "has-a" relationship where objects can exist independently and the container
object can exist without the contained objects.

Class Attributes:
Book:
- title: Book's title (string)
- author: Book's author (string)

Library:
- books: List of books in the library (list of Book objects)

Methods:
Book:
- __init__: Constructor - Initializes a new book

Library:
- __init__: Constructor - Initializes an empty library
- add_book: Adds a book to the library collection
- see_books: Displays all books in the library

Usage Example:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library = Library()
library.add_book(book1)  # Book exists independently of library
library.see_books()  # Prints: "The Great Gatsby by F. Scott Fitzgerald"
"""

class Book:
    """
    A class to represent a book with title and author.
    
    Attributes:
        title (str): Book's title
        author (str): Book's author
    """
    
    def __init__(self, title, author):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): Book's title
            author (str): Book's author
        """
        self.title = title
        self.author = author

class Library:
    """
    A class to represent a library that can contain multiple books.
    
    Attributes:
        books (list): List of Book objects in the library
    """

    def __init__(self):
        """
        Initialize a new Library instance with an empty book collection.
        """
        self.books : list[Book] = []

    def add_book(self, book: Book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book to add to the library
        """
        self.books.append(book)

    def see_books(self):
        """
        Display all books in the library.
        
        Output format: Prints each book as "Title by Author" on separate lines
        """
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Create library
library = Library()

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.see_books()

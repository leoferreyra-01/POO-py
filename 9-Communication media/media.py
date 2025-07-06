"""
Media Class Hierarchy Documentation

Overview:
This module implements a class hierarchy for different types of communication media using abstraction and polymorphism.
The abstract base class Media defines common characteristics, while concrete subclasses (Book, Magazine, Newspaper)
provide specific implementations for different media types.

Abstract Base Class:
- Media: Abstract base class with common attributes (title, author, date) and abstract describe() method

Concrete Classes:
- Book: Represents books with pages and genre information
- Magazine: Represents magazines with topic and periodicity
- Newspaper: Represents newspapers with news focus and publication frequency

Class Attributes:
- title: Media title (string)
- author: Media author/creator (string)  
- date: Publication date (string)

Methods:
- __init__: Constructor - Initializes media with basic information
- describe: Abstract method - Subclasses must implement to provide specific details

Usage Example:
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 180, "Classic")
magazine = Magazine("National Geographic", "National Geographic Society", "2024", "Nature", "Monthly")
newspaper = Newspaper("The New York Times", "The New York Times Company", "2024", "Politics", "Daily")

media_list = [book, magazine, newspaper]
for media in media_list:
    media.describe()  # Polymorphic behavior
"""

from abc import ABC, abstractmethod

class Media(ABC):
  """
  Abstract base class for different types of communication media.
  
  This class defines the common interface and attributes that all media types
  must have. The describe() method is abstract and must be implemented by
  concrete subclasses.
  
  Attributes:
      title (str): The title of the media
      author (str): The author or creator of the media
      date (str): The publication date of the media
  """
  
  def __init__(self, title, author, date):
    """
    Initialize a new Media instance.
    
    Args:
        title (str): The title of the media
        author (str): The author or creator of the media
        date (str): The publication date of the media
    """
    self.title = title
    self.author = author
    self.date = date
    
  @abstractmethod
  def describe(self):
    """
    Abstract method to describe the media.
    
    This method must be implemented by concrete subclasses to provide
    specific details about each type of media.
    """
    pass

class Book(Media):
  """
  A class to represent a book, inheriting from Media.
  
  Books have additional attributes like number of pages and genre,
  and provide a specific implementation of the describe() method.
  
  Attributes:
      pages (int): Number of pages in the book
      genre (str): Literary genre of the book
  """
  
  def __init__(self, title, author, date, pages, genre):
    """
    Initialize a new Book instance.
    
    Args:
        title (str): The title of the book
        author (str): The author of the book
        date (str): The publication date of the book
        pages (int): Number of pages in the book
        genre (str): Literary genre of the book
    """
    super().__init__(title, author, date)
    self.pages = pages
    self.genre = genre

  def describe(self):
    """
    Describe the book with its specific attributes.
    
    Prints formatted information about the book including title, author,
    publication date, number of pages, and genre.
    """
    print(f"Book: {self.title} by {self.author} ({self.date})")
    print(f"This book has {self.pages} pages and is a {self.genre} book.")

class Magazine(Media):
  """
  A class to represent a magazine, inheriting from Media.
  
  Magazines have additional attributes like topic and periodicity,
  and provide a specific implementation of the describe() method.
  
  Attributes:
      topic (str): Main topic or subject of the magazine
      periodicity (str): Publication frequency (e.g., "Monthly", "Weekly")
  """

  def __init__(self, title, author, date, topic, periodicity):
    """
    Initialize a new Magazine instance.
    
    Args:
        title (str): The title of the magazine
        author (str): The publisher or organization behind the magazine
        date (str): The publication date of the magazine
        topic (str): Main topic or subject of the magazine
        periodicity (str): Publication frequency
    """
    super().__init__(title, author, date)
    self.topic = topic
    self.periodicity = periodicity

  def describe(self):
    """
    Describe the magazine with its specific attributes.
    
    Prints formatted information about the magazine including title, author,
    publication date, topic, and periodicity.
    """
    print(f"Magazine: {self.title} by {self.author} ({self.date})")
    print(f"This magazine is about {self.topic} and is published {self.periodicity}.")

class Newspaper(Media):
  """
  A class to represent a newspaper, inheriting from Media.
  
  Newspapers have additional attributes like topic and periodicity,
  and provide a specific implementation of the describe() method
  focused on news content and daily/weekly frequency.
  
  Attributes:
      topic (str): Main news topic or subject of the newspaper
      periodicity (str): Publication frequency (e.g., "Daily", "Weekly")
  """

  def __init__(self, title, author, date, topic, periodicity):
    """
    Initialize a new Newspaper instance.
    
    Args:
        title (str): The title of the newspaper
        author (str): The publishing company or organization
        date (str): The publication date of the newspaper
        topic (str): Main news topic or subject of the newspaper
        periodicity (str): Publication frequency
    """
    super().__init__(title, author, date)
    self.topic = topic
    self.periodicity = periodicity

  def describe(self):
    """
    Describe the newspaper with its specific attributes.
    
    Prints formatted information about the newspaper including title, author,
    publication date, current news topic, and publication frequency.
    Focuses on news content and daily/weekly nature of newspapers.
    """
    print(f"Newspaper: {self.title} by {self.author} ({self.date})")
    print(f"Today's topic is {self.topic}.")
    print(f"Remember that this newspaper is published {self.periodicity}.")

def main():
  """
  Main function to demonstrate polymorphism with different media types.
  
  Creates instances of Book, Magazine, and Newspaper classes,
  stores them in a list, and demonstrates polymorphic behavior
  by calling the describe() method on each media object.
  """
  book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 180, "Classic")
  magazine1 = Magazine("National Geographic", "National Geographic Society", "2024", "Nature", "Monthly")
  newspaper1 = Newspaper("The New York Times", "The New York Times Company", "2024", "Politics", "Daily")

  media_list = [book1, magazine1, newspaper1]

  for media in media_list:
    media.describe()
    print()

if __name__ == "__main__":
  main()

Case

It is required to design and develop a class hierarchy that represents different types of communication media. You will use polymorphism to allow uniform interaction with all types of media through a common interface, and apply abstraction to define a base class that encapsulates the common characteristics of these media.

 
Instructions

    Create a file called `media.py` in which you will be working on this activity

    Then, create an abstract class called Medium that includes common attributes such as title, author, and publication date. Additionally, define an abstract method describe() that subclasses must implement to provide specific details about the medium.

    Implementation of Child Classes:
    Book Class: Derives from Medium and implements the describe() method to include details such as genre and number of pages.
    
    Magazine Class: Derives from Medium and adds attributes such as topic and periodicity. Its implementation of describe() must handle these new attributes.

    Newspaper Class: Similar to Magazine, but must differentiate itself in how it presents its description, focusing on news and daily or weekly frequency.

    Ensure that the describe() method can be used polymorphically in a context where the specific type of communication medium is not known, such as in an array of Medium.

    Write a script that creates instances of each type of medium, adds them to a list, and then iterates over that list invoking the describe() method to demonstrate polymorphism.

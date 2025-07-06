"""
Person Class Documentation

Overview:
The Person class demonstrates encapsulation principles by managing person information with controlled access to age through getters and setters.

Class Attributes:
- name: Person's name (public attribute)
- __age: Person's age (private attribute - encapsulated)
- gender: Person's gender (public attribute)

Methods:
- __init__: Constructor - Initializes a new person
- Age (property): Getter - Returns the person's age
- Age (setter): Setter - Validates and sets the person's age

Encapsulation Features:
- Private age attribute (__age) prevents direct external access
- Property decorator provides controlled access to age
- Age validation ensures only positive values are accepted

Usage Example:
person = Person("John", 20, "Male")
print(person.Age)  # 20
person.Age = 21    # Valid age
person.Age = -5    # Invalid age - prints error message
"""

class Person:
    """
    A class to represent a person with encapsulated age management.
    
    This class demonstrates encapsulation by using private attributes
    and property decorators to control access to sensitive data.
    
    Attributes:
        name (str): Person's name (public)
        __age (int): Person's age (private - encapsulated)
        gender (str): Person's gender (public)
    """

    def __init__(self, att_name, att_age, att_gender):
        """
        Initialize a new Person instance.
        
        Args:
            att_name (str): Person's name
            att_age (int): Person's age (must be positive)
            att_gender (str): Person's gender
        """
        self.name = att_name
        self.__age = att_age
        self.gender = att_gender

    @property # getter
    def Age(self):
        """
        Get the person's age.
        
        Returns:
            int: The person's current age
        """
        return self.__age

    @Age.setter # setter
    def Age(self, age):
        """
        Set the person's age with validation.
        
        Only positive age values are accepted. Invalid values
        will trigger an error message without changing the age.
        
        Args:
            age (int): New age value to set
        """
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
  
p1 = Person("John", 20, "Male")
# print(p1.__age)  # This should return an error
print(p1.Age)
p1.Age = 21
print(p1.Age)
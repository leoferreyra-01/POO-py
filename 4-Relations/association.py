"""
Association Relationship Documentation

Overview:
This module demonstrates the Association relationship between Teacher and Subject classes.
Association is a "uses-a" relationship where objects can exist independently but can be linked.

Class Attributes:
Subject:
- name: Subject's name (string)
- teacher: List of teachers assigned to this subject

Teacher:
- name: Teacher's name (string)
- age: Teacher's age (integer)
- subject: Currently assigned subject (Subject object)

Methods:
Subject:
- __init__: Constructor - Initializes a new subject
- change_name: Updates the subject's name
- see_teachers: Prints all teachers assigned to this subject

Teacher:
- __init__: Constructor - Initializes a new teacher
- assign_subject: Links teacher to a subject (bidirectional association)

Usage Example:
subject1 = Subject("Math")
teacher1 = Teacher("John", 30)
teacher1.assign_subject(subject1)  # Creates association between teacher and subject
print(teacher1.subject.name)  # "Math"
subject1.change_name("Maths")  # Updates subject name
print(teacher1.subject.name)  # "Maths" (shows shared reference)
subject1.see_teachers()  # Prints "John"
"""

class Subject:
    """
    A class to represent a subject that can be taught by multiple teachers.
    
    Attributes:
        name (str): Subject's name
        teacher (list): List of teachers assigned to this subject
    """
    
    def __init__(self, name):
        """
        Initialize a new Subject instance.
        
        Args:
            name (str): Subject's name
        """
        self.name = name
        self.teacher = []

    def change_name(self, name):
        """
        Update the subject's name.
        
        Args:
            name (str): New name for the subject
        """
        self.name = name

    def see_teachers(self):
        """
        Print all teachers assigned to this subject.
        
        Output format: Prints each teacher's name on a separate line
        """
        for teacher in self.teacher:
            print(teacher.name)


class Teacher:
    """
    A class to represent a teacher who can be assigned to teach subjects.
    
    Attributes:
        name (str): Teacher's name
        age (int): Teacher's age
        subject (Subject): Currently assigned subject (can be None)
    """
    
    def __init__(self, name, age):
        """
        Initialize a new Teacher instance.
        
        Args:
            name (str): Teacher's name
            age (int): Teacher's age
        """
        self.name = name
        self.age = age
        self.subject : Subject 

    def assign_subject(self, subject: Subject):
        """
        Assign a subject to the teacher (creates bidirectional association).
        
        Args:
            subject (Subject): The subject to assign to this teacher
        """
        self.subject = subject
        subject.teacher.append(self)



# Create subject
subject1=Subject("Math")


# Create teachers
teacher1=Teacher("John", 30)
teacher2=Teacher("Jane", 32)

# Assign subject to teacher
teacher1.assign_subject(subject1)

print(teacher1.subject.name)

subject1.change_name("Maths")

print(teacher1.subject.name)

subject1.see_teachers()
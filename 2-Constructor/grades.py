"""
Student Class Documentation

Overview:
The Student class manages student information including grades, calculates averages, and determines approval status.

Class Attributes:
- grades_options: List of valid grades (0-10)
- grades: List of student's grades
- name: Student's name (string)
- id: Student's unique identifier (integer)
- age: Student's age (integer)

Methods:
- __init__: Constructor - Initializes a new student
- average: Returns arithmetic mean of all grades
- is_approved: Returns True if average >= 6.0, False otherwise
- add_note: Appends valid grade to student's grade list
- see_info: Prints formatted student information

Usage Example:
student = Student("John", 1, 20, [8, 7, 9])
student.add_note(10)
student.see_info()  # Prints student details
print(student.is_approved())  # True (average = 8.5)
"""

class Student:
	"""
	A class to represent a student with grades and approval status.
	
	Attributes:
		grades_options (list): Valid grade range (0-10)
		grades (list): Student's grades
		name (str): Student's name
		id (int): Unique student identifier
		age (int): Student's age
	"""

	grades_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	grades : list[int]
	name : str
	id : int
	age : int
	
	
	def __init__(self, name, id, age, grades):
		"""
		Initialize a new Student instance.
		
		Args:
			name (str): Student's name
			id (int): Unique student ID
			age (int): Student's age
			grades (list): List of grades (0-10)
		"""
		self.name = name
		self.id = id 
		self.age = age
		self.grades = grades if all(grade in self.grades_options for grade in grades) else []

	def average(self):
		"""
		Calculate the arithmetic mean of all grades.
		
		Returns:
			float: The average grade
		"""
		return sum(self.grades) / len(self.grades)

	def is_approved(self):
		"""
		Check if student passes based on grade threshold.
		
		Returns:
			bool: True if average >= 6.0, False otherwise
		"""
		return self.average() >= 6.0

	def add_note(self, grade):
		"""
		Add a valid grade to the student's grade list.
		
		Args:
			grade (int): Grade to add (must be 0-10)
		"""
		if grade in self.grades_options:
			self.grades.append(grade)
	
	def see_info(self):
		"""
		Print formatted student information.
		
		Output format: "Name: {name}, ID: {id}, Age: {age}, Grades: {grades}, Average: {average}"
		"""
		print(f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Grades: {self.grades}, Average: {self.average()}")


student1 = Student("Juan", 1, 20, [10, 7, 6])
student2 = Student("Pedro", 2, 21, [5, 3, 9])
student3 = Student("Maria", 3, 22, [7, 3, 6])

students : list[Student] = [student1, student2, student3]

while True:

	print("--------------------------------")
	print("1. Add student")
	print("2. See students")
	print("3. Add grade")
	print("4. See student info")
	print("5. Check if approved")
	print("6. Exit")

	opcion = int(input("Enter an option: "))

	if opcion == 1:
		name = input("Enter the student name: ")
		while True:
			try:
				id = int(input("Enter the student ID: "))
				if id <= 0:
					print("Invalid ID. Please enter a positive number.")
					continue
				if any(student.id == id for student in students):
					print("The ID already exists. Please enter a different ID.")
					continue
				break
			except ValueError:
				print("Invalid ID. Please enter a valid number.")
		age = int(input("Enter the student age: "))
		print("Enter the student grades: ")
		grades : list[int] = []

		for i in range(3):
			while True:
				grade = int(input(f"Enter the grade {i+1}: "))
				if grade in Student.grades_options:
					grades.append(grade)
					break
				else:
					print("Invalid grade. Please enter a grade between 0 and 10.")

		student : Student = Student(name, id, age, grades)
		students.append(student)

	if opcion == 2:
		if len(students) == 0:
			print("No students")
		else:
			for student in students:
				student.see_info()

	if opcion == 3 or opcion == 4 or opcion == 5:
		id = int(input("Enter the student ID: "))
		student_found = False

		for student in students:
			if student.id == id:
				student_found = True
				if opcion == 3:
					grade = int(input("Enter the grade: "))
					student.add_note(grade)
				if opcion == 4:
					student.see_info()
				if opcion == 5:
					is_approved = student.is_approved()
					if is_approved:
						print(f"The student passed with {student.average()}")
					else:
						print(f"The student did not pass with {student.average()}")
				break
		
		if not student_found:
			print("Student not found with that ID.")

	if opcion == 6:
		break
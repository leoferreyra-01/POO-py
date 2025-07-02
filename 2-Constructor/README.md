# Constructor Exercise: Student Grade Management System

This exercise focuses on **constructor methods** (`__init__`) and practical application of Object-Oriented Programming concepts through a complete student grade management system.

## 📁 Files in this Exercise

- `grades.py` - Main student grade management system
- `main.py` - Additional constructor examples
- `README.md` - This documentation

## 🏫 Student Class Overview

The `Student` class demonstrates a complete OOP implementation with:

### Class Attributes
```python
grades_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Valid grade range
grades: list[int]    # Student's grades
name: str           # Student's name
id: int             # Unique student identifier
age: int            # Student's age
```

### Constructor Method
```python
def __init__(self, name, id, age, grades):
    """
    Initialize a new Student instance with validation.
    
    Args:
        name (str): Student's name
        id (int): Unique student ID
        age (int): Student's age
        grades (list): List of grades (0-10)
    """
```

### Key Methods
- **`average()`**: Calculates grade average
- **`is_approved()`**: Checks if student passes (average ≥ 6.0)
- **`add_note(grade)`**: Adds valid grade to student's record
- **`see_info()`**: Displays formatted student information

## 🚀 How to Run the Exercise

### Step 1: Navigate to the Directory
```bash
cd "2-Constructor"
```

### Step 2: Run the Main Program
```bash
python grades.py
```

### Step 3: Follow the Interactive Menu

The program will display a menu with these options:

```
--------------------------------
1. Add student
2. See students
3. Add grade
4. See student info
5. Check if approved
6. Exit
```

## 📋 Menu Options Explained

### 1. Add Student
- **Purpose**: Create a new student with validation
- **Inputs Required**:
  - Student name (text)
  - Student ID (positive integer, must be unique)
  - Student age (integer)
  - Three grades (0-10 each)
- **Validation**: Ensures ID is unique and grades are valid

### 2. See Students
- **Purpose**: Display all registered students
- **Output**: Shows name, ID, age, grades, and average for each student
- **Note**: Shows "No students" if list is empty

### 3. Add Grade
- **Purpose**: Add a new grade to an existing student
- **Process**:
  1. Enter student ID
  2. Enter new grade (0-10)
  3. Grade is added to student's record
- **Validation**: Checks if student exists and grade is valid

### 4. See Student Info
- **Purpose**: View detailed information of a specific student
- **Process**: Enter student ID to see their complete information
- **Output**: Formatted display of student data

### 5. Check if Approved
- **Purpose**: Verify if a student passes based on their average
- **Process**: Enter student ID to check approval status
- **Output**: Shows whether student passed or failed with their average

### 6. Exit
- **Purpose**: Close the application
- **Note**: All data is lost when program exits (in-memory storage)

## 🔧 Input Validation Features

### Student ID Validation
- Must be a positive integer
- Must be unique (no duplicates allowed)
- Handles non-numeric input gracefully

### Grade Validation
- Must be between 0 and 10 (inclusive)
- Program keeps asking until valid grade is entered
- Clear error messages guide the user

### Student Search
- Shows "Student not found" for non-existent IDs
- Prevents errors when searching for missing students

## 🎓 Pre-loaded Students

The program starts with three sample students:

1. **Juan** (ID: 1, Age: 20) - Grades: [10, 7, 6] - Average: 7.67
2. **Pedro** (ID: 2, Age: 21) - Grades: [5, 3, 9] - Average: 5.67
3. **Maria** (ID: 3, Age: 22) - Grades: [7, 3, 6] - Average: 5.33
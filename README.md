# POO-py: Object-Oriented Programming Practice

A Python project for practicing Object-Oriented Programming (OOP) concepts through various exercises and examples.

## 📁 Project Structure

```
POO-py/
├── 1-Classes and Objects/
│   └── main.py
├── 2-Constructor/
│   ├── grades.py
│   ├── main.py
│   └── README.md
├── 3-Encapsulation/
│   └── main.py
├── 4-Relations/
│   ├── association.py
│   ├── aggregation.py
│   └── composition.py
├── 5-Inheritance/
│   └── Inheritance.py
└── README.md
```

## 🎯 Overview

This project contains multiple exercises and examples to help you learn and practice Object-Oriented Programming concepts in Python. Each folder contains different exercises focusing on specific OOP concepts.

## 📚 Available Exercises

### 1. Classes and Objects (`1-Classes and Objects/`)
- **File**: `main.py`
- **Focus**: Basic class definition and object creation
- **Concepts**: Classes, objects, attributes, methods

### 2. Constructor (`2-Constructor/`)
- **Files**: `grades.py`, `main.py`
- **Focus**: Constructor methods and practical application
- **Concepts**: `__init__` method, parameter validation, interactive applications

#### Student Grade Management System
The main exercise in this section is a complete student grade management system that demonstrates:
- Class constructors with validation
- Data encapsulation
- Method implementation
- User input handling
- Error management

### 3. Encapsulation (`3-Encapsulation/`)
- **File**: `main.py`
- **Focus**: Data encapsulation and access control
- **Concepts**: Private attributes, property decorators, getters and setters

#### Person Class with Encapsulated Age
This exercise demonstrates encapsulation principles through a Person class that:
- Uses private attributes (`__age`) to prevent direct external access
- Implements property decorators for controlled access to sensitive data
- Provides validation in setters to ensure data integrity
- Shows how encapsulation protects data while maintaining controlled access

### 4. Object Relationships (`4-Relations/`)
- **Files**: `association.py`, `aggregation.py`, `composition.py`
- **Focus**: Different types of relationships between objects
- **Concepts**: Association, Aggregation, Composition relationships

#### Association Relationship (`association.py`)
Demonstrates a "uses-a" relationship where objects can exist independently but can be linked:
- Teacher and Subject classes with bidirectional association
- Objects can exist independently and be linked later
- Shows shared references and how changes propagate

#### Aggregation Relationship (`aggregation.py`)
Demonstrates a "has-a" relationship where objects can exist independently:
- Library and Book classes showing container relationship
- Books can exist without being in a library
- Loose coupling between container and contained objects

#### Composition Relationship (`composition.py`)
Demonstrates a "part-of" relationship where parts cannot exist independently:
- Car, Engine, and Wheels classes showing strong dependency
- Parts are created and destroyed with the whole object
- Strong coupling where parts cannot exist without the container

### 5. Inheritance (`5-Inheritance/`)
- **File**: `Inheritance.py`
- **Focus**: Class inheritance and method overriding
- **Concepts**: Single inheritance, multiple inheritance, method overriding, super() function

#### Vehicle Inheritance Hierarchy
This exercise demonstrates inheritance concepts through a comprehensive vehicle class hierarchy:
- **Vehicle**: Base class with brand and model attributes
- **Electric**: Base class for electric functionality with battery capacity
- **Car**: Single inheritance example extending Vehicle with color
- **Motorcycle**: Single inheritance example extending Vehicle with engine capacity
- **Truck**: Multi-level inheritance example extending Car with load capacity
- **ElectricCar**: Multiple inheritance example combining Car and Electric features

#### Key Inheritance Concepts Demonstrated:
- **Single Inheritance**: Car and Motorcycle inheriting from Vehicle
- **Multiple Inheritance**: ElectricCar inheriting from both Car and Electric
- **Multi-level Inheritance**: Truck inheriting from Car, which inherits from Vehicle
- **Method Overriding**: ElectricCar's see_info method overriding Vehicle's version
- **Constructor Chaining**: Using `super()` and explicit parent class calls
- **Method Chaining**: Calling parent methods from child classes

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your computer
- Basic understanding of Python syntax

### Step-by-Step Setup

#### Step 1: Clone or Download the Project
```bash
# If using Git:
git clone <repository-url>

# Or download and extract the ZIP file to your desired location
```

#### Step 2: Verify Python Installation
Open your terminal/command prompt and run:
```bash
python --version
# or
python3 --version
```
You should see Python 3.6 or higher.

#### Step 3: Navigate to the Project Directory
```bash
cd POO-py
```

#### Step 4: Choose an Exercise to Practice

**Option A: Start with Basic Classes and Objects**
```bash
cd "1-Clases y objetos"
python main.py
```

**Option B: Practice with Constructor Exercise**
```bash
cd "2-Constructor"
python grades.py
```

**Option C: Practice with Encapsulation Exercise**
```bash
cd "3-Encapsulation"
python main.py
```

**Option D: Practice with Object Relationships**
```bash
cd "4-Relations"
# Association relationship
python association.py

# Aggregation relationship  
python aggregation.py

# Composition relationship
python composition.py
```

**Option E: Practice with Inheritance**
```bash
cd "5-Inheritance"
python Inheritance.py
```

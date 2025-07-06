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
├── 6-RPG/
│   ├── main.py
│   └── README.md
├── 7-Polymorphism/
│   └── polymorphism.py
├── 8-Abstraction/
│   └── abstraction.py
├── 9-Communication media/
│   ├── media.py
│   └── README.md
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

### 6. RPG System (`6-RPG/`)
- **File**: `main.py`
- **Focus**: Comprehensive RPG system with proper encapsulation and inheritance
- **Concepts**: Encapsulation, inheritance, class associations, battle system, weapon management

#### Role-Playing Game Class System
This exercise implements a complete RPG system that demonstrates advanced OOP concepts:
- **Weapon Class**: Represents weapons with name and power attributes
- **Character Class**: Base class with health, level, and weapon management
- **Enemy Class**: Inherits from Character with bonus damage and enemy types
- **Ally Class**: Inherits from Character with healing bonuses and ally types

#### Key Features Implemented:
- **Proper Encapsulation**: All attributes are private with getters/setters
- **Input Validation**: Health bounds, level validation, damage constraints
- **Weapon System**: Characters can equip weapons that affect battle damage
- **Battle Mechanics**: Attack system using weapon power + character level
- **Specialization**: Enemies get damage bonuses, Allies get healing bonuses
- **Health Management**: Healing system with validation and defeat detection
- **Class Associations**: Characters can have weapons equipped
- **Method Overriding**: Specialized attack and heal methods in subclasses

#### Encapsulation Examples:
- Private attributes (`__name`, `__health`, `__weapon`, etc.)
- Controlled access through getters/setters
- Data validation in setters
- Protection against invalid states

### 7. Polymorphism (`7-Polymorphism/`)
- **File**: `polymorphism.py`
- **Focus**: Polymorphism through method overriding and interface uniformity
- **Concepts**: Method overriding, interface polymorphism, runtime polymorphism

#### Payment System Polymorphism
This exercise demonstrates polymorphism concepts through a payment system where different payment methods can be treated uniformly:
- **CreditCard Class**: Represents credit card payments with card details
- **PayPal Class**: Represents PayPal payments with account credentials
- **Common Interface**: Both classes implement a `pay()` method with different behaviors

#### Key Polymorphism Concepts Demonstrated:
- **Method Overriding**: Both CreditCard and PayPal implement `pay()` with different behaviors
- **Interface Polymorphism**: Different objects can be treated uniformly through common methods
- **Runtime Polymorphism**: The same method call produces different results based on object type
- **Collection Polymorphism**: Processing different payment methods in a single loop

#### Polymorphism Examples:
- Same method name (`pay`) with different implementations
- Uniform treatment of different object types
- Dynamic method resolution at runtime
- Code reusability through common interfaces

### 8. Abstraction (`8-Abstraction/`)
- **File**: `abstraction.py`
- **Focus**: Abstract classes and method abstraction
- **Concepts**: Abstract base classes, abstract methods, interface definition, implementation hiding

#### Vehicle Abstraction System
This exercise demonstrates abstraction concepts through an abstract Vehicle class that defines a common interface for different vehicle types:
- **Vehicle (Abstract)**: Base class that cannot be instantiated directly
- **Car**: Concrete implementation extending Vehicle with color attribute
- **Motorcycle**: Concrete implementation extending Vehicle with engine capacity

#### Key Abstraction Concepts Demonstrated:
- **Abstract Base Class**: Vehicle class that cannot be instantiated directly
- **Abstract Methods**: `move()` method that must be implemented by subclasses
- **Interface Definition**: Common interface for all vehicle types
- **Implementation Hiding**: Concrete implementations are hidden behind abstract interface
- **Template Pattern**: Abstract class provides structure for concrete classes

#### Abstraction Examples:
- Abstract class definition using `ABC` and `@abstractmethod`
- Forced implementation of abstract methods in subclasses
- Common interface definition across different vehicle types
- Separation of interface from implementation details

### 9. Communication Media (`9-Communication media/`)
- **File**: `media.py`
- **Focus**: Class hierarchy with abstraction and polymorphism for communication media
- **Concepts**: Abstract base classes, inheritance, polymorphism, interface uniformity

#### Media Class Hierarchy System
This exercise demonstrates a comprehensive class hierarchy for different types of communication media, combining abstraction and polymorphism concepts:
- **Media (Abstract)**: Base abstract class with common attributes (title, author, date)
- **Book**: Concrete implementation with pages and genre information
- **Magazine**: Concrete implementation with topic and periodicity
- **Newspaper**: Concrete implementation with news focus and publication frequency

#### Key Features Implemented:
- **Abstract Base Class**: Media class that cannot be instantiated directly
- **Abstract Methods**: `describe()` method that must be implemented by all subclasses
- **Inheritance Hierarchy**: All media types inherit from the abstract Media class
- **Polymorphic Behavior**: Uniform interface through the `describe()` method
- **Specialized Implementations**: Each media type provides unique description format

#### Abstraction and Polymorphism Concepts Demonstrated:
- **Abstract Class Definition**: Using `ABC` and `@abstractmethod` decorators
- **Common Interface**: All media types implement the same `describe()` method
- **Polymorphic Collections**: Processing different media types in a single list
- **Method Overriding**: Each subclass provides its own `describe()` implementation
- **Interface Uniformity**: Different objects can be treated uniformly through common methods

#### Media Types and Their Characteristics:
- **Book**: Focuses on literary content with pages and genre information
- **Magazine**: Emphasizes topic and publication frequency
- **Newspaper**: Highlights news content and daily/weekly publication nature

#### Polymorphism Examples:
- Same method name (`describe`) with different implementations across media types
- Uniform treatment of different media objects in collections
- Dynamic method resolution based on object type at runtime
- Code reusability through common abstract interface

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

**Option F: Practice with RPG System**
```bash
cd "6-RPG"
python main.py
```

**Option G: Practice with Polymorphism**
```bash
cd "7-Polymorphism"
python polymorphism.py
```

**Option H: Practice with Abstraction**
```bash
cd "8-Abstraction"
python abstraction.py
```

**Option I: Practice with Communication Media**
```bash
cd "9-Communication media"
python media.py
```

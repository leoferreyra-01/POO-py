"""
Abstraction Demonstration Documentation

Overview:
This module demonstrates abstraction in object-oriented programming through an abstract Vehicle class
that defines a common interface for different vehicle types. The abstract class cannot be instantiated
directly but provides a template for concrete vehicle implementations.

Class Attributes:
- Vehicle (Abstract): brand, model (abstract base class)
- Car: brand, model (inherited), color (specific to car)
- Motorcycle: brand, model (inherited), cc (specific to motorcycle)

Methods:
- Vehicle.__init__: Constructor - Initializes a new vehicle (abstract base)
- Vehicle.move: Abstract method - Must be implemented by subclasses
- Vehicle.see_info: Prints vehicle brand and model information
- Car.__init__: Constructor - Initializes a new car with color
- Car.move: Concrete implementation - Car-specific movement behavior
- Car.see_color: Prints the car's color
- Motorcycle.__init__: Constructor - Initializes a new motorcycle with engine capacity
- Motorcycle.move: Concrete implementation - Motorcycle-specific movement behavior
- Motorcycle.see_cc: Prints the motorcycle's engine capacity

Abstraction Concepts Demonstrated:
- Abstract Base Class: Vehicle class that cannot be instantiated directly
- Abstract Methods: move() method that must be implemented by subclasses
- Interface Definition: Common interface for all vehicle types
- Implementation Hiding: Concrete implementations are hidden behind abstract interface
- Template Pattern: Abstract class provides structure for concrete classes

Usage Example:
# This would raise an error - Vehicle is abstract
# vehicle = Vehicle("Ford", "Mustang")

car1 = Car("Ford", "Mustang", "Red")
motorcycle1 = Motorcycle("Honda", "CBR", 1000)

car1.move()  # "The car is moving"
car1.see_info()  # "Brand: Ford, Model: Mustang"

motorcycle1.move()  # "The motorcycle is moving"
motorcycle1.see_info()  # "Brand: Honda, Model: CBR"
"""

from abc import ABC, abstractmethod

#Father Class
class Vehicle(ABC):
	"""
	A base class to represent a generic vehicle.
	
	This class serves as the parent class for all vehicle types.
	It provides basic vehicle information including brand and model.
	
	Attributes:
		brand (str): The brand name of the vehicle
		model (str): The model name of the vehicle
	"""

	def __init__(self, brand, model):
		"""
		Initialize a new Vehicle instance.
		
		Args:
			brand (str): The brand name of the vehicle
			model (str): The model name of the vehicle
		"""
		self.brand = brand
		self.model = model

	@abstractmethod
	def move(self):
		"""
		Abstract method that must be implemented by subclasses.
		
		This method defines the interface for vehicle movement.
		Each concrete vehicle class must provide its own implementation.
		"""
		pass

	def see_info(self):
		"""
		Print the vehicle's brand and model information.
		
		Output format: "Brand: {brand}, Model: {model}"
		"""
		print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
	"""
	A class to represent a car, inheriting from Vehicle.
	
	This class extends the Vehicle class by adding car-specific
	attributes like color. It demonstrates single inheritance.
	
	Attributes:
		brand (str): Inherited from Vehicle - The brand name
		model (str): Inherited from Vehicle - The model name
		color (str): The color of the car
	"""

	def __init__(self, brand, model, color):
		"""
		Initialize a new Car instance.
		
		Uses super() to call the parent class constructor and
		then adds the car-specific color attribute.
		
		Args:
			brand (str): The brand name of the car
			model (str): The model name of the car
			color (str): The color of the car
		"""
		super().__init__(brand, model) #super() is used to call the constructor of the parent class
		self.color = color

	def move(self):
		"""
		Concrete implementation of the abstract move method.
		
		Output: Prints car-specific movement message
		"""
		print("The car is moving")

	def see_color(self):
		"""
		Print the car's color information.
		
		Output format: "Color: {color}"
		"""
		print(f"Color: {self.color}")

class Motorcycle(Vehicle):
	"""
	A class to represent a motorcycle, inheriting from Vehicle.
	
	This class extends the Vehicle class by adding motorcycle-specific
	attributes like engine capacity (cc). It demonstrates single inheritance.
	
	Attributes:
		brand (str): Inherited from Vehicle - The brand name
		model (str): Inherited from Vehicle - The model name
		cc (int): Engine capacity in cubic centimeters
	"""

	def __init__(self, brand, model, cc):
		"""
		Initialize a new Motorcycle instance.
		
		Uses super() to call the parent class constructor and
		then adds the motorcycle-specific cc attribute.
		
		Args:
			brand (str): The brand name of the motorcycle
			model (str): The model name of the motorcycle
			cc (int): Engine capacity in cubic centimeters
		"""
		super().__init__(brand, model)
		self.cc = cc

	def move(self):
		"""
		Concrete implementation of the abstract move method.
		
		Output: Prints motorcycle-specific movement message
		"""
		print("The motorcycle is moving")

	def see_cc(self):
		"""
		Print the motorcycle's engine capacity.
		
		Output format: "CC: {cc}"
		"""
		print(f"CC: {self.cc}")

# Example usage demonstrating abstraction
print("=== Abstraction Demonstration ===")
print("Note: Vehicle class is abstract and cannot be instantiated directly")
print("# vehicle = Vehicle('Ford', 'Mustang')  # This would raise an error\n")

print("=== Concrete Vehicle Implementations ===")
car1 = Car("Ford", "Mustang", "Red")
motorcycle1 = Motorcycle("Honda", "CBR", 1000)

print("Car demonstration:")
car1.move()
car1.see_info()
car1.see_color()

print("\nMotorcycle demonstration:")
motorcycle1.move()
motorcycle1.see_info()
motorcycle1.see_cc()






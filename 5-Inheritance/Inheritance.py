"""
Inheritance Example Documentation

Overview:
This file demonstrates inheritance concepts in Python, including single inheritance, multiple inheritance, and method overriding. It shows how classes can inherit from parent classes and extend their functionality.

Class Hierarchy:
- Vehicle (Base Class): Represents a generic vehicle with brand and model
- Electric (Base Class): Represents electric functionality with battery capacity
- Car (Child of Vehicle): Represents a car with additional color attribute
- Motorcycle (Child of Vehicle): Represents a motorcycle with engine capacity (cc)
- Truck (Child of Car): Represents a truck with load capacity
- ElectricCar (Child of Car and Electric): Demonstrates multiple inheritance

Class Attributes:
Vehicle:
- brand: Vehicle brand name (string)
- model: Vehicle model name (string)

Electric:
- battery: Battery capacity (string)

Car:
- brand, model: Inherited from Vehicle
- color: Car color (string)

Motorcycle:
- brand, model: Inherited from Vehicle
- cc: Engine capacity in cubic centimeters (integer)

Truck:
- brand, model: Inherited from Vehicle via Car
- color: Inherited from Car
- load_capacity: Maximum load capacity in kilograms (integer)

ElectricCar:
- brand, model: Inherited from Vehicle via Car
- color: Inherited from Car
- battery: Inherited from Electric

Methods:
Vehicle:
- __init__: Constructor - Initializes brand and model
- see_info: Prints brand and model information

Electric:
- __init__: Constructor - Initializes battery capacity
- see_battery: Prints battery information

Car:
- __init__: Constructor - Calls parent constructor and adds color
- see_color: Prints car color

Motorcycle:
- __init__: Constructor - Calls parent constructor and adds cc
- see_cc: Prints engine capacity

Truck:
- __init__: Constructor - Calls parent constructor and adds load capacity
- see_load_capacity: Prints comprehensive truck information

ElectricCar:
- __init__: Constructor - Initializes from both parent classes
- see_info: Overrides parent method to show all information

Usage Examples:
truck1 = Truck('Ford', 'F-150', 'Black', 1000)
truck1.see_load_capacity()  # Prints: Brand: Ford, Model: F-150, Color: Black, Load Capacity: 1000 kg

car1 = ElectricCar('Tesla', 'Model 3', 'Red', '100kWh')
car1.see_info()  # Prints: Brand: Tesla, Model: Model 3, Color: Red, Battery: 100kWh
"""

#Father Class
class Vehicle:
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

    def see_info(self):
        """
        Print the vehicle's brand and model information.
        
        Output format: "Brand: {brand}, Model: {model}"
        """
        print(f"Brand: {self.brand}, Model: {self.model}")

#Father Class
class Electric():
    """
    A base class to represent electric functionality.
    
    This class provides electric vehicle capabilities including
    battery management and information display.
    
    Attributes:
        battery (str): The battery capacity of the electric vehicle
    """

    def __init__(self, battery):
        """
        Initialize a new Electric instance.
        
        Args:
            battery (str): The battery capacity (e.g., '100kWh')
        """
        self.battery = battery

    def see_battery(self):
        """
        Print the battery capacity information.
        
        Output format: "Battery: {battery}"
        """
        print(f"Battery: {self.battery}")

#Child Class
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

    def see_color(self):
        """
        Print the car's color information.
        
        Output format: "Color: {color}"
        """
        print(f"Color: {self.color}")

#Child Class
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

    def see_cc(self):
        """
        Print the motorcycle's engine capacity.
        
        Output format: "CC: {cc}"
        """
        print(f"CC: {self.cc}")

class Truck(Car):
    """
    A class to represent a truck, inheriting from Car.
    
    This class extends the Car class by adding truck-specific
    attributes like load capacity. It demonstrates inheritance
    through multiple levels (Vehicle -> Car -> Truck).
    
    Attributes:
        brand (str): Inherited from Vehicle via Car - The brand name
        model (str): Inherited from Vehicle via Car - The model name
        color (str): Inherited from Car - The color of the truck
        load_capacity (int): Maximum load capacity in kilograms
    """

    def __init__(self, brand, model, color, load_capacity):
        """
        Initialize a new Truck instance.
        
        Uses super() to call the parent Car class constructor and
        then adds the truck-specific load_capacity attribute.
        
        Args:
            brand (str): The brand name of the truck
            model (str): The model name of the truck
            color (str): The color of the truck
            load_capacity (int): Maximum load capacity in kilograms
        """
        super().__init__(brand, model, color)
        self.load_capacity = load_capacity

    def see_load_capacity(self):
        """
        Print comprehensive information about the truck.
        
        This method calls parent class methods to display brand,
        model, and color information, then adds the load capacity.
        
        Output format: 
        "Brand: {brand}, Model: {model}"
        "Color: {color}"
        "Load Capacity: {load_capacity} kg"
        """
        super().see_info()
        super().see_color()
        print(f"Load Capacity: {self.load_capacity} kg")

class ElectricCar(Car, Electric):
    """
    A class to represent an electric car with multiple inheritance.
    
    This class inherits from both Car and Electric classes, demonstrating
    multiple inheritance. It combines car features (brand, model, color)
    with electric features (battery capacity).
    
    Attributes:
        brand (str): Inherited from Vehicle via Car - The brand name
        model (str): Inherited from Vehicle via Car - The model name
        color (str): Inherited from Car - The color of the car
        battery (str): Inherited from Electric - The battery capacity
    """

    def __init__(self, brand, model, color, battery):
        """
        Initialize a new ElectricCar instance.
        
        Uses explicit parent class constructors to initialize
        attributes from both Car and Electric classes.
        
        Args:
            brand (str): The brand name of the electric car
            model (str): The model name of the electric car
            color (str): The color of the electric car
            battery (str): The battery capacity (e.g., '100kWh')
        """
        Car.__init__(self, brand, model, color)
        Electric.__init__(self, battery)

    def see_info(self):
        """
        Print comprehensive information about the electric car.
        
        This method overrides the parent Vehicle.see_info() method
        to display all relevant information including brand, model,
        color, and battery capacity.
        
        Output format: 
        "Brand: {brand}, Model: {model}"
        "Color: {color}"
        "Battery: {battery}"
        """
        Car.see_info(self)
        Car.see_color(self)
        Electric.see_battery(self)

print("Truck:")
truck1 = Truck('Ford', 'F-150', 'Black', 1000)
truck1.see_load_capacity()

print("\n")
print("Electric Car:")
car1 = ElectricCar('Tesla', 'Model 3', 'Red', '100kWh')
car1.see_info()
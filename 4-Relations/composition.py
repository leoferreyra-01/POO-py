"""
Composition Relationship Documentation

Overview:
This module demonstrates the Composition relationship between Car, Engine, and Wheels classes.
Composition is a "part-of" relationship where the contained objects are created and destroyed
with the container object. The parts cannot exist independently of the whole.

Class Attributes:
Engine:
- power: Engine's power (integer)

Wheels:
- size: Wheel's size (integer)

Car:
- engine: Engine instance (Engine object)
- wheels: List of wheel instances (list of Wheels objects)

Methods:
Engine:
- __init__: Constructor - Initializes a new engine

Wheels:
- __init__: Constructor - Initializes a new wheel

Car:
- __init__: Constructor - Initializes a car with engine and wheels
- see_engine_power: Displays the engine's power
- see_wheels_size: Displays the size of all wheels

Usage Example:
car1 = Car(120, 16)  # Creates car with engine(power=120) and 4 wheels(size=16)
car1.see_engine_power()  # Prints: 120
car1.see_wheels_size()   # Prints: 16 (4 times, one for each wheel)
"""

class Engine:
    """
    A class to represent a car engine.
    
    Attributes:
        power (int): Engine's power
    """

    def __init__(self, power):
        """
        Initialize a new Engine instance.
        
        Args:
            power (int): Engine's power
        """
        self.power = power

class Wheels:
    """
    A class to represent a car wheel.
    
    Attributes:
        size (int): Wheel's size
    """

    def __init__(self, size):
        """
        Initialize a new Wheels instance.
        
        Args:
            size (int): Wheel's size
        """
        self.size = size

class Car:
    """
    A class to represent a car composed of engine and wheels.
    
    Attributes:
        engine (Engine): The car's engine
        wheels (list): List of wheel objects (always 4 wheels)
    """

    def __init__(self, power, size):
        """
        Initialize a new Car instance with engine and wheels.
        
        Args:
            power (int): Engine power for the car
            size (int): Size for all wheels of the car
        """
        self.engine = Engine(power)
        self.wheels = [Wheels(size) for _ in range(4)]

    def see_engine_power(self):
        """
        Display the engine's power.
        
        Output format: Prints the engine power value
        """
        print(self.engine.power)

    def see_wheels_size(self):
        """
        Display the size of all wheels.
        
        Output format: Prints each wheel's size on separate lines (4 lines total)
        """
        for wheel in self.wheels:
            print(wheel.size)


car1 = Car(120, 16)
car2 = Car(100, 14)

car1.see_engine_power()
car1.see_wheels_size()

car2.see_engine_power()
car2.see_wheels_size()


Case

The design and development of a class system for a role-playing game (RPG) is required, which will incorporate characters, enemies, and weapons. It is essential to apply the principles of encapsulation and inheritance to structure the code in a way that is efficient and easy to maintain.

 
Instructions

    Create your small development environment in order to carry out this activity in the correct way.

    Create a Python file called `poo_role_play.py`

    Define a Character class with attributes such as name, level, and health. Include a constructor method to initialize these attributes and methods to receive damage or heal.

    Define an Enemy class that inherits from Character and add specific attributes such as type (for example, zombie, vampire) and damage.

    Ensure that the class attributes are properly encapsulated (Define which ones to encapsulate and which ones not to). Use access modifiers to control the visibility of attributes and methods, ensuring that data manipulation can only be done through public methods (getters and setters).

    Create at least one additional subclass of Character that represents another type of entity in the game, such as Ally, with unique characteristics.

    Implement methods that demonstrate code reuse through inheritance and specialization of behaviors.

    Define a Weapon class with attributes such as name and power. Associate this class with Character so that each character can have a weapon equipped.

    Write a small script that creates instances of your classes and demonstrates the interaction between them, such as battles between characters and enemies using weapons.

    Implement interactions between characters and enemies using weapons, for example, an attack method that uses the weapon's power to reduce the enemy's health.

    Make sure to test all methods and encapsulation verifications, especially the correct functioning of getters and setters.

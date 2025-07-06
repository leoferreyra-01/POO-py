"""
RPG Class System with Proper Encapsulation

This file implements a role-playing game system with proper encapsulation,
inheritance, and class interactions as specified in the requirements.
"""

class Weapon:
    """
    A class to represent weapons in the RPG system.
    
    Attributes:
        __name (str): Private weapon name
        __power (int): Private weapon power/damage
    """
    
    def __init__(self, name, power):
        """
        Initialize a new Weapon instance.
        
        Args:
            name (str): The name of the weapon
            power (int): The power/damage of the weapon
        """
        self.__name = name
        self.__power = power
    
    # Getters
    def get_name(self):
        """Get the weapon name."""
        return self.__name
    
    def get_power(self):
        """Get the weapon power."""
        return self.__power
    
    # Setters
    def set_name(self, name):
        """Set the weapon name."""
        self.__name = name
    
    def set_power(self, power):
        """Set the weapon power."""
        if power >= 0:
            self.__power = power
        else:
            print("Power cannot be negative.")
    
    def display_info(self):
        """Display weapon information."""
        print(f"Weapon: {self.__name}, Power: {self.__power}")

class Character:
    """
    A base class to represent characters in the RPG system.
    
    Attributes:
        __name (str): Private character name
        __health (int): Private current health
        __max_health (int): Private maximum health
        __level (int): Private character level
        __weapon (Weapon): Private equipped weapon
    """
    
    def __init__(self, name, health, level):
        """
        Initialize a new Character instance.
        
        Args:
            name (str): The character's name
            health (int): The character's health
            level (int): The character's level
        """
        self.__name = name
        self.__max_health = health
        self.__health = health
        self.__level = level
        self.__weapon = None
    
    # Getters
    def get_name(self):
        """Get the character's name."""
        return self.__name
    
    def get_health(self):
        """Get the character's current health."""
        return self.__health
    
    def get_max_health(self):
        """Get the character's maximum health."""
        return self.__max_health
    
    def get_level(self):
        """Get the character's level."""
        return self.__level
    
    def get_weapon(self):
        """Get the character's equipped weapon."""
        return self.__weapon
    
    # Setters
    def set_name(self, name):
        """Set the character's name."""
        self.__name = name
    
    def set_health(self, health):
        """Set the character's health with validation."""
        if health < 0:
            self.__health = 0
        elif health > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health = health
    
    def set_level(self, level):
        """Set the character's level."""
        if level > 0:
            self.__level = level
        else:
            print("Level must be positive.")
    
    def equip_weapon(self, weapon):
        """Equip a weapon to the character."""
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
            print(f"{self.__name} equipped {weapon.get_name()}!")
        else:
            print("Invalid weapon object.")
    
    def heal(self, amount):
        """
        Heal the character by the specified amount.
        
        Args:
            amount (int): Amount of health to restore
        """
        if self.__health == self.__max_health:
            print(f"{self.__name} is already at full health.")
        else:
            old_health = self.__health
            self.set_health(self.__health + amount)
            actual_healed = self.__health - old_health
            print(f"{self.__name} has been healed by {actual_healed} points.")
    
    def take_damage(self, amount):
        """
        Take damage and reduce health.
        
        Args:
            amount (int): Amount of damage to take
        """
        old_health = self.__health
        self.set_health(self.__health - amount)
        actual_damage = old_health - self.__health
        print(f"{self.__name} has taken {actual_damage} damage.")
        
        if self.__health == 0:
            print(f"{self.__name} has been defeated!")
    
    def attack(self, target):
        """
        Attack another character using the equipped weapon.
        
        Args:
            target (Character): The target to attack
        """
        if self.__weapon is None:
            print(f"{self.__name} has no weapon equipped!")
            return
        
        if self.__health <= 0:
            print(f"{self.__name} cannot attack while defeated!")
            return
        
        damage = self.__weapon.get_power() + self.__level
        print(f"{self.__name} attacks {target.get_name()} with {self.__weapon.get_name()}!")
        target.take_damage(damage)
    
    def see_health(self):
        """Display the character's health information."""
        print(f"{self.__name} has {self.__health}/{self.__max_health} health points.")
    
    def is_alive(self):
        """Check if the character is alive."""
        return self.__health > 0

class Enemy(Character):
    """
    A class to represent enemies, inheriting from Character.
    
    Attributes:
        __type (str): Private enemy type
        __base_damage (int): Private base damage bonus
    """
    
    def __init__(self, name, health, level, enemy_type):
        """
        Initialize a new Enemy instance.
        
        Args:
            name (str): The enemy's name
            health (int): The enemy's health
            level (int): The enemy's level
            enemy_type (str): The type of enemy (zombie, vampire, etc.)
        """
        super().__init__(name, health, level)
        self.__type = enemy_type
        self.__base_damage = 5  # Enemies get bonus damage
    
    # Getters
    def get_type(self):
        """Get the enemy type."""
        return self.__type
    
    def get_base_damage(self):
        """Get the enemy's base damage bonus."""
        return self.__base_damage
    
    # Setters
    def set_type(self, enemy_type):
        """Set the enemy type."""
        self.__type = enemy_type
    
    def set_base_damage(self, damage):
        """Set the enemy's base damage bonus."""
        if damage >= 0:
            self.__base_damage = damage
        else:
            print("Base damage cannot be negative.")
    
    def attack(self, target):
        """
        Override attack method to include base damage bonus.
        
        Args:
            target (Character): The target to attack
        """
        weapon = self.get_weapon()
        if weapon is None:
            print(f"{self.get_name()} has no weapon equipped!")
            return
        
        if self.get_health() <= 0:
            print(f"{self.get_name()} cannot attack while defeated!")
            return
        
        damage = weapon.get_power() + self.get_level() + self.__base_damage
        print(f"{self.get_name()} attacks {target.get_name()} with {weapon.get_name()}!")
        target.take_damage(damage)
    
    def see_type(self):
        """Display the enemy type."""
        print(f"{self.get_name()} is a {self.__type} enemy.")

class Ally(Character):
    """
    A class to represent allies, inheriting from Character.
    
    Attributes:
        __type (str): Private ally type
        __healing_bonus (int): Private healing bonus
    """
    
    def __init__(self, name, health, level, ally_type):
        """
        Initialize a new Ally instance.
        
        Args:
            name (str): The ally's name
            health (int): The ally's health
            level (int): The ally's level
            ally_type (str): The type of ally (healer, warrior, etc.)
        """
        super().__init__(name, health, level)
        self.__type = ally_type
        self.__healing_bonus = 3  # Allies get healing bonus
    
    # Getters
    def get_type(self):
        """Get the ally type."""
        return self.__type
    
    def get_healing_bonus(self):
        """Get the ally's healing bonus."""
        return self.__healing_bonus
    
    # Setters
    def set_type(self, ally_type):
        """Set the ally type."""
        self.__type = ally_type
    
    def set_healing_bonus(self, bonus):
        """Set the ally's healing bonus."""
        if bonus >= 0:
            self.__healing_bonus = bonus
        else:
            print("Healing bonus cannot be negative.")
    
    def heal(self, amount):
        """
        Override heal method to include healing bonus.
        
        Args:
            amount (int): Amount of health to restore
        """
        if self.get_health() == self.get_max_health():
            print(f"{self.get_name()} is already at full health.")
        else:
            old_health = self.get_health()
            self.set_health(self.get_health() + amount + self.__healing_bonus)
            actual_healed = self.get_health() - old_health
            print(f"{self.get_name()} has been healed by {actual_healed} points (including {self.__healing_bonus} bonus).")
    
    def heal_ally(self, target, amount):
        """
        Heal another character with bonus healing.
        
        Args:
            target (Character): The target to heal
            amount (int): Amount of health to restore
        """
        if self.get_health() <= 0:
            print(f"{self.get_name()} cannot heal while defeated!")
            return
        
        if target.get_health() == target.get_max_health():
            print(f"{target.get_name()} is already at full health.")
        else:
            old_health = target.get_health()
            target.set_health(target.get_health() + amount + self.__healing_bonus)
            actual_healed = target.get_health() - old_health
            print(f"{self.get_name()} heals {target.get_name()} by {actual_healed} points (including {self.__healing_bonus} bonus).")
    
    def see_type(self):
        """Display the ally type."""
        print(f"{self.get_name()} is a {self.__type} ally.")

# Demo script to test all functionality
def main():
    """Main function to demonstrate the RPG system."""
    print("=== RPG System Demo ===\n")
    
    # Create weapons
    sword = Weapon("Iron Sword", 15)
    axe = Weapon("Battle Axe", 20)
    staff = Weapon("Healing Staff", 10)
    
    # Create characters
    hero = Ally("Arthur", 100, 5, "Warrior")
    enemy = Enemy("Dark Knight", 80, 4, "Undead")
    
    # Equip weapons
    hero.equip_weapon(sword)
    enemy.equip_weapon(axe)
    
    # Display initial information
    print("Initial Status:")
    hero.see_health()
    enemy.see_health()
    hero.see_type()
    enemy.see_type()
    print()
    
    # Battle demonstration
    print("=== Battle Begins ===")
    hero.attack(enemy)
    enemy.see_health()
    print()
    
    enemy.attack(hero)
    hero.see_health()
    print()
    
    # Healing demonstration
    print("=== Healing ===")
    hero.heal(20)
    hero.see_health()
    print()
    
    # Test encapsulation
    print("=== Testing Encapsulation ===")
    print(f"Hero name: {hero.get_name()}")
    print(f"Hero health: {hero.get_health()}")
    print(f"Enemy type: {enemy.get_type()}")
    
    # Test invalid operations
    print("\n=== Testing Validation ===")
    hero.set_health(-10)  # Should set to 0
    hero.see_health()
    hero.set_health(200)  # Should set to max health
    hero.see_health()

if __name__ == "__main__":
    main()

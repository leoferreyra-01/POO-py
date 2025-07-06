"""
Polymorphism Demonstration Documentation

Overview:
This module demonstrates polymorphism in object-oriented programming through a payment system
where different payment methods (CreditCard and PayPal) can be treated uniformly through
a common interface.

Class Attributes:
- CreditCard: name, card_number, expiration_date, cvv (all private)
- PayPal: email, password (all private)

Methods:
- CreditCard.__init__: Constructor - Initializes a new credit card
- CreditCard.get_name: Returns the cardholder's name
- CreditCard.get_card_number: Returns the card number
- CreditCard.get_expiration_date: Returns the expiration date
- CreditCard.get_cvv: Returns the CVV code
- CreditCard.pay: Processes payment with credit card
- PayPal.__init__: Constructor - Initializes a new PayPal account
- PayPal.get_email: Returns the PayPal email
- PayPal.get_password: Returns the PayPal password
- PayPal.pay: Processes payment with PayPal

Polymorphism Concepts Demonstrated:
- Method Overriding: Both classes implement a 'pay' method with different behaviors
- Interface Polymorphism: Different objects can be treated uniformly through common methods
- Runtime Polymorphism: The same method call produces different results based on object type

Usage Example:
method1 = CreditCard("John Doe", "1234567890", "12/2025", "123")
method2 = PayPal("john.doe@example.com", "password123")
method1.pay(100)  # "Paying 100 with credit card"
method2.pay(100)  # "Paying 100 with PayPal"

# Polymorphic behavior with list of different payment methods
payment_methods = [method1, method2]
for method in payment_methods:
    method.pay(50)  # Same method call, different implementations
"""

from random import Random


class CreditCard:
	"""
	A class to represent a credit card payment method.
	
	Attributes:
		__name (str): Cardholder's name (private)
		__card_number (str): Credit card number (private)
		__expiration_date (str): Card expiration date (private)
		__cvv (str): Card verification value (private)
	"""

	def __init__(self, name, card_number, expiration_date, cvv):
		"""
		Initialize a new CreditCard instance.
		
		Args:
			name (str): Cardholder's name
			card_number (str): Credit card number
			expiration_date (str): Card expiration date
			cvv (str): Card verification value
		"""
		self.__name = name
		self.__card_number = card_number
		self.__expiration_date = expiration_date
		self.__cvv = cvv

	def get_name(self):
		"""
		Get the cardholder's name.
		
		Returns:
			str: The cardholder's name
		"""
		return self.__name

	def get_card_number(self):
		"""
		Get the credit card number.
		
		Returns:
			str: The credit card number
		"""
		return self.__card_number

	def get_expiration_date(self):
		"""
		Get the card expiration date.
		
		Returns:
			str: The expiration date
		"""
		return self.__expiration_date

	def get_cvv(self):
		"""
		Get the card verification value.
		
		Returns:
			str: The CVV code
		"""
		return self.__cvv

	def pay(self, amount):
		"""
		Process payment using credit card.
		
		Args:
			amount (int/float): Payment amount
		
		Output: Prints payment confirmation message
		"""
		print(f"Paying {amount} with credit card")

class PayPal:
	"""
	A class to represent a PayPal payment method.
	
	Attributes:
		__email (str): PayPal account email (private)
		__password (str): PayPal account password (private)
	"""

	def __init__(self, email, password):
		"""
		Initialize a new PayPal instance.
		
		Args:
			email (str): PayPal account email
			password (str): PayPal account password
		"""
		self.__email = email
		self.__password = password

	def get_email(self):
		"""
		Get the PayPal account email.
		
		Returns:
			str: The PayPal email address
		"""
		return self.__email

	def get_password(self):
		"""
		Get the PayPal account password.
		
		Returns:
			str: The PayPal password
		"""
		return self.__password

	def pay(self, amount):
		"""
		Process payment using PayPal.
		
		Args:
			amount (int/float): Payment amount
		
		Output: Prints payment confirmation message
		"""
		print(f"Paying {amount} with PayPal")

# Example usage demonstrating polymorphism
method1 = CreditCard("John Doe", "1234567890", "12/2025", "123")
method2 = PayPal("john.doe@example.com", "password123")

print("=== Individual Payment Methods ===")
method1.pay(100)
method2.pay(100)

print("\n=== Polymorphic Payment Processing ===")
payment_methods = [
	CreditCard("John Doe", "1234567890", "12/2025", "123"),
	CreditCard("Jane Doe", "0987654321", "06/2026", "456"),
	PayPal("john.doe@example.com", "password123"),
	PayPal("jane.doe@example.com", "password456")
]

for method in payment_methods:
	method.pay(Random().randint(1, 100))
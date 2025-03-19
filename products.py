
class Product:
	def __init__(self, name: str, price: float, quantity: int):
		# Validate inputs
		if not name:
			raise ValueError("Product name cannot be empty.")
		if price < 0:
			raise ValueError("Price cannot be negative.")
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")

		self.name = name
		self.price = price
		self.quantity = quantity
		# This way by default, a new product will be activated
		self.active = True


	def get_quantity(self) -> int:
		return self.quantity

	def set_quantity(self, quantity: int):
		# Update the quantity
		self.quantity = quantity

		# If quantity has reached 0, deactivate the product
		if self.quantity == 0:
			# Deactivates the product
			self.deactivate()

	def is_active(self) -> bool:
		return self.active
		#return True

	def activate(self):
		# Activates the product
		self.active = True

	def deactivate(self):
		# Deactivates the product
		self.active = False

	def show(self) -> str:
		"""
		Returns a string that represents the product.
		Example: "MacBook Air M2, Price: 1450, Quantity: 100"
		"""
		return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

	def buy(self, quantity: int) -> float:
		"""
		Buys a given quantity of the product
		Returns the total price (float) of the purchase.
		Updates the quantity of the product.
		In case of a problem (when? think about it), raises an Exception.
		"""
		# Raising an exception in case of a problem
		# Validating inputs
		if not self.active:
			raise Exception("Cannot buy an inactive product.")
		if quantity <= 0:
			raise ValueError("Purchase quantity must be positive")
		if quantity > self.quantity:
			raise ValueError("Not enough items in stock.")

		# Calculate total price
		total_price = self.price * quantity

		# Update quantity
		self.set_quantity(self.quantity - quantity)

		# Return total price
		return total_price


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(bose.is_active())
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
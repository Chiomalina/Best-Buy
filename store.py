import products

class Store:
	def __init__(self, products_list):
		"""
		Initialize the store with a list of Product objects.
		"""
		self._products = products_list


	def add_product(self, product):
		"""
		Add a new product to the store's list of products.
		"""
		self._products.append(product)


	def remove_product(self, product):
		"""
		Remove a product from the store's list of products.
		"""
		self._products.remove(product)

	def get_total_quantity(self) -> int:
		"""
		Returns how many items are in the store in total.
		(The sum of quantities across all products.)
		"""
		return sum(product.get_quantity() for product in self._products)

	def get_all_products(self) -> list:
		"""
		Returns a list of all *active* products in the store.
		(Active means p.is_active() is True.)
		"""

		#return [p for p in self._products if p.is_active()]
		active_products = []
		for product in self._products:
			if product.is_active():
				active_products.append(product)
		return active_products

	def order(self, shopping_list) -> float:
		"""
		Takes a list of tuples (Product, quantity).
		Buys the requested number of each product and returns
		the total price of the order.
		"""
		total_price = 0
		for product, quantity in shopping_list:
			# Buy the specific quantity from each product
			cost = product.buy(quantity)
			total_price += cost
		return total_price

	def __str__(self) -> str:
		"""
		Returns a human-readable string representation of the store and its products.
		"""
		# Display basic store info: total products, total quantity, and then list each product on a new line.
		store_summary = str(
			f"Store with {len(self._products)} products. "
			f"Total quantity in store: {self.get_total_quantity()}.\n"
			"Active Products:\n"
		)

		# List the active products.
		active_products = self.get_all_products()
		for product in active_products:
			#print(active_products)
			store_summary += f" {str(product)}\n"
		return store_summary

def main(products_module=None):

	product_list = [
		products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

	best_buy = Store(product_list)
	print(best_buy)
	# active_products = best_buy.get_all_products()
	# total_quantity = best_buy.get_total_quantity()
	# print(active_products)
	# print(total_quantity)

	# Print total quantity
	#print("Total quantity in store:", best_buy.get_total_quantity())
	# print("Total quantity in store:", total_quantity)
	#
	# print(best_buy.order([
	# 	(active_products[0], 1), (active_products[1], 2)
	# ]))


if __name__ == "__main__":
	main()
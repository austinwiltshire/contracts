class ValueStock(object):
	"""A stock is a value stock if its Price to Book ratio is below 1"""
	def __init__(self, price, book_value):
		self._price = price
		self._book_value = book_value
		self._invariant()

	def _invariant_(self):
		assert self._price < self._book_value, "Value stocks must have prices below book values"

	def buy(self):
		self._invariant()
		...
		self._invariant()

	def sell(self):
		self._invariant()
		...
		self._invariant()

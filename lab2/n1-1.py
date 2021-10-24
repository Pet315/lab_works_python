class Rectangle:
	"""Class Rectangle"""

	def __init__(self, length=1, width=1):
		self.length = length
		self.width = width

	def __str__(self):
		return f'a: {self.length}, b: {self.width}'

	@property
	def length(self):
		return self.__length

	@length.setter
	def length(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError("Error 1")
		if value < 0.0 or value > 20.0:
			raise ValueError("Error 3")
		self.__length = value

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if not isinstance(value, (int, float)):
			raise TypeError("Error 1")
		if value < 0.0 or value > 20.0:
			raise ValueError("Error 3")
		self.__width = value

	def func1(self):
		perimeter = 2*(self.__length + self.__width)
		return perimeter

	def func2(self):
		area = self.__length * self.__width
		return area

x = Rectangle()
print(str(x))
print(x.func1(), x.func2())

x = Rectangle(19.9, 5)
print(x.func1(), x.func2())

# x = Rectangle(20.9, 5)
# print(x.func1(), x.func2())
# x.set()

# x = Rectangle(-2, 5)
# print(x.func1(), x.func2())
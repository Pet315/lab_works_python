class Rectangle:
	"""Class Rectangle"""

	# part 1
	def __init__(self, length=1, width=1):
		if length > 0 and width > 0:
			self.length = length
			self.width = width
		else:
			print("Error 1")
			exit(1)
	def func1(self):
		perimeter = 2*(self.length + self.width)
		return perimeter
	def func2(self):
		area = self.length * self.width
		return area

	# part 2
	def getter(self):
		return self.length, self.width
	def setter(self, a, b):
		self.length = a
		self.width = b
		if self.length < 0.0 or self.length > 20.0 or self.width < 0.0 or self.width > 20.0:
			print("Error 2")
			exit(1)
		else:
			return True



# x = Rectangle(-2,5)
# print(x.func1(), x.func2())

x = Rectangle()
print(x.func1(), x.func2())
x = Rectangle(2,5)
print(x.func1(), x.func2())

print(x.getter())
print(x.setter(19.9, 13.3))
print(x.setter(29.9, 13.3))
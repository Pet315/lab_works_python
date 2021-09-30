class Rational:
	"""Class Rational"""
	index = 0
	# part 1
	def __init__(self, num=1, den=1):
		self.num = num
		self.den = den
	def func1(self, a, b):
		self.num = a
		self.den = b
		return str(int(self.num))+'/'+str(int(self.den))
	def func2(self):
		self.num = a
		self.den = b
		return self.num/self.den

x = Rational()
print(x.func1(1,2))
print(x.func2(1,2))
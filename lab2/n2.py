import math
class Rational:
	"""Class Rational"""
	index = 0
	# part 1
	def __init__(self, num=4, den=16):
		try:
			isinstance(num, int)
			isinstance(den, int)
		except:
			exit(1)
		if not den:
			exit(1)
		index = math.gcd(num, den)
		self.num = num/index
		self.den = den/index

	def func1(self):
		return str(self.num)+' / '+str(self.den)
	def func2(self):
		return self.num/self.den

x = Rational()
print(x.func1(), x.func2(), sep="\n")
x = Rational(3,0)
print(x.func1(), x.func2(), sep="\n")

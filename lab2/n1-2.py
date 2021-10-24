import math
class Rational:
	"""Class Rational"""
	# part 1
	def __init__(self, num=4, den=16):
		if not isinstance(num, (int, float)) or not isinstance(den, (int, float)):
			raise TypeError("Error 1")
		if not den:
			raise ZeroDivisionError("Error 2")
		i = math.gcd(num, den)
		self.num = num//i
		self.den = den//i

	def func1(self):
		return str(self.num)+' / '+str(self.den)
	def func2(self):
		return self.num/self.den

x = Rational()
print(x.func1(), x.func2(), sep="\n")

# x = Rational(3, 0)
# print(x.func1(), x.func2(), sep="\n")
# x = Rational('fdb', 2)
# print(x.func1(), x.func2(), sep="\n")
class Rational:
    """Class Rational"""

    def __init__(self, num=4, den=16):
        self.num = num
        self.den = den
        self.shrink()

    def shrink(self):
        i = gcd(self.num, self.den)
        self.num = self.num // i
        self.den = self.den // i

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        self.__num = value

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        if not value:
            raise ZeroDivisionError("Error 4")
        self.__den = value

    def __str__(self):
        return f'{self.num} / {self.den}'

    def div(self):
        return self.num / self.den

    def __add__(self, other):
        if isinstance(other, (Rational, int)):
            num1 = self.num*other.den + other.num*self.den
            den1 = self.den * other.den
            return Rational(num1, den1)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (Rational, int)):
            num1 = self.num * other.den - other.num * self.den
            den1 = self.den * other.den
            return Rational(num1, den1)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (Rational, int)):
            num1 = self.num * other.num
            den1 = self.den * other.den
            return Rational(num1, den1)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num*other.den < other.num*self.den
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num*other.den > other.num*self.den
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num*other.den == other.num*self.den
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num*other.den != other.num*self.den
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num * other.den >= other.num*self.den
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (Rational, int)):
            return self.num*other.den <= other.num*self.den
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, (Rational, int)):
            self.num = self.num * other.den + other.num * self.den
            self.den = self.den * other.den
            self.shrink()
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, (Rational, int)):
            self.num = self.num * other.den - other.num * self.den
            self.den = self.den * other.den
            self.shrink()
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (Rational, int)):
            self.num = self.num * other.den
            self.den = self.den * other.den
            self.shrink()
            return self
        return NotImplemented


x1 = Rational()
x2 = Rational(8, 16)
# x3 = Rational(25, 5)
y1 = x1 + x2
print(str(y1), y1.div())
x1 += x2
x1 *= x2
print(x1.div())
if x1 <= x2:
    print('completed')

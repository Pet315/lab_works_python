import math


class Rational:
    """Class Rational"""

    def __init__(self, num=4, den=16):
        i = math.gcd(num, den)
        self.num = num // i
        self.den = den // i

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 3")
        self.__num = value

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 3")
        if not value:
            raise ZeroDivisionError("Error 4")
        self.__den = value

    def __str__(self):
        return f'{self.num} / {self.den}'

    def div(self):
        return self.num / self.den

    def __add__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den + other.num/other.den
        raise TypeError("Error 2")

    def __sub__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den - other.num/other.den
        raise TypeError("Error 2")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den * other.num/other.den
        raise TypeError("Error 2")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den / other.num/other.den
        raise TypeError("Error 2")

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den < other.num/other.den
        raise TypeError("Error 2")

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den > other.num/other.den
        raise TypeError("Error 2")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den == other.num/other.den
        raise TypeError("Error 2")

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den != other.num/other.den
        raise TypeError("Error 2")

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den >= other.num/other.den
        raise TypeError("Error 2")

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.num/self.den <= other.num/other.den
        raise TypeError("Error 2")

    def __iadd__(self, other):
        if isinstance(other, Rational):
            a = self.num/self.den
            b = other.num/other.den
            a += b
            return a
        raise TypeError("Error 2")

    def __isub__(self, other):
        if isinstance(other, Rational):
            a = self.num / self.den
            b = other.num / other.den
            a -= b
            return a
        raise TypeError("Error 2")

    def __imul__(self, other):
        if isinstance(other, Rational):
            a = self.num / self.den
            b = other.num / other.den
            a *= b
            return a
        raise TypeError("Error 2")

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            a = self.num / self.den
            b = other.num / other.den
            a /= b
            return a
        raise TypeError("Error 2")


x1 = Rational()
x2 = Rational(8, 16)
x3 = Rational(25, 5)
print(str(x1), x1.div())
print(x2 + x1, x1 - x2, x1 * x2, x1 / x3)
print(x1 > x2, x1 < x2, x1 != x2, x1 == x2, x1 >= x2, x1 <= x2)
x1 *= x2
print(x1)

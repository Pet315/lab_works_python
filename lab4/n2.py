import data


class Good:
    """Class Good"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 2")
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 2")
        self.__quantity = value

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("Error 5")
        self.quantity += other
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Error 5")
        self.quantity -= other
        return self

    def __imul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Error 5")
        self.price *= other
        return self

    def __itruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Error 5")
        self.price /= other
        return self


class Composition:
    """Class Composition"""

    def __init__(self, goods):
        self.goods = goods

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, goods):
        if not all([isinstance(gd, Good) for gd in goods]):
            raise TypeError("Error 6")
        self.__goods = goods

    def __eq__(self, data):
        if not isinstance(data, str):
            raise TypeError("Error 6")
        for gd in self.goods:
            if gd.name == data:
                return gd

    def __iadd__(self, other):
        if not isinstance(other, Good):
            raise TypeError("Error 6")
        self.goods.append(other)
        return self

    def all_price(self):
        all_pr = 0
        for gd in self.goods:
            all_pr += gd.price
        return all_pr

    def __str__(self):
        basket = []
        for gd in self.goods:
            basket.append(str(gd))
        return str(basket)


x1 = Good('table', 1000, 245)
x2 = Good('chair', 350, 655)
x3 = Good('sofa', 20000, 12)
y1 = Composition([x1, x2, x3])
print(x1)
x1 += 17
print(x1)
x1 *= 2.5
print(x1)
print(y1)
y1 += Good('commode', 3094.5, 35)
print(y1)
print(y1 == 'chair')
print(y1.all_price())

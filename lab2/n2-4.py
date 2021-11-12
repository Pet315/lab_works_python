class BinTr:
    """ Class Tree """

    def __init__(self, code, price):
        self.right = None
        self.left = None
        self.code = code
        self.price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 2")
        self.__code = value

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

    def insert(self, code, cost):
        if code == self.code:
            raise ValueError("Error 3")
        if code < self.code:
            if not self.left:
                self.left = BinTr(code, cost)
            else:
                self.left.insert(code, cost)
        elif code > self.code:
            if not self.right:
                self.right = BinTr(code, cost)
            else:
                self.right.insert(code, cost)

    def return_price(self, code):
        if code < self.code:
            if not self.left:
                raise ValueError("Error 4")
            else:
                return self.left.return_price(code)
        elif code > self.code:
            if not self.right:
                raise ValueError("Error 4")
            else:
                return self.right.return_price(code)
        else:
            return self.price


x = BinTr(0, 0)
x.insert(1, 150)
x.insert(2, 250)
x.insert(3, 350)
x.insert(4, 450)
try:
    c1 = int(input("Code: "))
    q1 = int(input("Number of products: "))
    price = x.return_price(c1)
    print(price * q1)
except ValueError:
    raise ValueError("Error 5")
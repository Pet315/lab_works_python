class Product:
    """Class Product"""

    def __init__(self, price, description, proportions):
        self.price = price
        self.description = description
        self.proportions = proportions

    def __str__(self):
        return f'pr: {self.price}, ds: {self.description}, pp: {self.proportions}'

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
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__description = value

    @property
    def proportions(self):
        return self.__proportions

    @proportions.setter
    def proportions(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 2")
        self.__proportions = value


class Customer:
    """Class Customer"""

    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'sr: {self.surname}, nm: {self.name}, pt: {self.patronymic}, mp: {self.mobile_phone}'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__surname = value

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
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__patronymic = value

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__mobile_phone = value


class Order:
    """Class Order"""
    all_price = 0

    def __init__(self, customer=None):
        if not isinstance(customer, Customer):
            raise TypeError("Error 5")
        self.customer = customer
        self.products = []

    def process(self, pr):
        if not isinstance(pr, Product):
            raise TypeError("Error 6")
        self.products.append(pr)

    def delete(self, pr):
        if not isinstance(pr, Product):
            raise TypeError("Error 6")
        self.products.remove(pr)

    def total_order(self):
        count = 0
        for pr in self.products:
            count += pr.price
        return count


pr1 = Product(3300, "multicooker", 24.6)
print(str(pr1))
pr2 = Product(11300, "washer", 44.3)
print(str(pr2))
pr3 = Product(16000, "cooler", 203.99)
print(str(pr3))
cus = Customer("Polehenko", "Viktor", "Andrijovych", "0653412408")
print(str(cus))
info1 = Order(cus)
info1.process(pr1)
info1.process(pr2)
info1.process(pr3)
info1.delete(pr2)
print(info1.total_order())

# a_cus = Customer("Irzhenko", "Anna", "Semenivna", 3741892435)

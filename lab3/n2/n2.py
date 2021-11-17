import json
import datetime

data1 = [
    {
        "pizza_name": "Margaritta",
        "squad": ['tomato sauce', 'mozzarella', 'oregano'],
        "possible_extra_ingredients": {"pineapple": 10, "mushrooms": 15, "ham": 20, "salami": 18},
        "value": 100
    },
    {
        "pizza_name": "Carbonara",
        "squad": ['tomato sauce', 'mozzarella', 'parmesan', 'eggs', 'bacon'],
        "possible_extra_ingredients": {"pesto": 32, "olives": 15, "capers": 17},
        "value": 160
    },
    {
        "pizza_name": "Marinara",
        "squad": ['tomato sauce', 'garlic', 'basil'],
        "possible_extra_ingredients": {"pesto": 32, "oregano": 15, "capers": 17},
        "value": 200
    },
    {
        "pizza_name": "Four seasons",
        "squad": ['tomato sauce', 'mozzarella', 'mushrooms'],
        "possible_extra_ingredients": {"ham": 20, "artichokes": 16, "olives": 15},
        "value": 370
    },
    {
        "pizza_name": "Napoletana",
        "squad": ['tomato sauce', 'mozzarella', 'oregano', 'anchovies'],
        "possible_extra_ingredients": {"olives": 15, "capers": 17},
        "value": 559
    },
    {
        "pizza_name": "Vegetariana",
        "squad": ['tomato sauce', 'mozzarella', 'basil'],
        "possible_extra_ingredients": {"olives": 15, "capers": 17, "zucchini": 22, "eggplant": 5, "pepper": 10},
        "value": 455
    },
    {
        "pizza_name": "Fattoria",
        "squad": ['tomato sauce', 'mozzarella', 'pepper'],
        "possible_extra_ingredients": {"peas": 25, "porchetta": 40, "zucchini": 22},
        "value": 155
    }
]
try:
    with open("data.json", "w") as wrfile:
        json.dump(data1, wrfile)
except FileNotFoundError:
    raise FileNotFoundError("Error 7")


class General:
    """
    Class General. You can find there all details, connected with pizza-of-the-day
    for each day and also there are all checks for class attributes
    """

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        self.person_name = person_name
        self.pizza_name = pizza_name
        self.price = price
        self.squad = squad
        self.extra_ingr = extra_ingr

    @property
    def pizza_name(self):
        return self.__pizza_name

    @pizza_name.setter
    def pizza_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 1")
        self.__pizza_name = value

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 1")
        self.__person_name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Error 2")
        if value < 0:
            raise ValueError("Error 3")
        self.__price = value

    @property
    def squad(self):
        return self.__squad

    @squad.setter
    def squad(self, value):
        if not all([isinstance(ingr, str) for ingr in value]):
            raise TypeError("Error 4")
        self.__squad = value

    @property
    def extra_ingr(self):
        return self.__extra_ingr

    @extra_ingr.setter
    def extra_ingr(self, dict):
        for element in dict.values():
            if not isinstance(element, (int, float)):
                raise TypeError("Error 5")
        for element in dict.keys():
            if not isinstance(element, str):
                raise TypeError("Error 6")
        self.__extra_ingr = dict


class Pizza1(General):

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        super().__init__(pizza_name, price, squad, person_name, extra_ingr)

    def __str__(self):
        return f'Monday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza2(General):

    def __init__(self, pizza_name, price, ingredients, person_name, extra_ingr):
        super().__init__(pizza_name, price, ingredients, person_name, extra_ingr)

    def __str__(self):
        return f'Tuesday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza3(General):

    def __init__(self, pizza_name, price, ingredients, person_name, extra_ingr):
        super().__init__(pizza_name, price, ingredients, person_name, extra_ingr)

    def __str__(self):
        return f'Wednesday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza4(General):

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        super().__init__(pizza_name, price, squad, person_name, extra_ingr)

    def __str__(self):
        return f'Thursday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza5(General):

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        super().__init__(pizza_name, price, squad, person_name, extra_ingr)

    def __str__(self):
        return f'Friday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza6(General):

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        super().__init__(pizza_name, price, squad, person_name, extra_ingr)

    def __str__(self):
        return f'Saturday: {self.pizza_name}, {self.price}, {self.squad}'


class Pizza7(General):

    def __init__(self, pizza_name, price, squad, person_name, extra_ingr):
        super().__init__(pizza_name, price, squad, person_name, extra_ingr)

    def __str__(self):
        return f'Sunday: {self.pizza_name}, {self.price}, {self.squad}'


class Order:
    """
    Class Order. It contains a possibility to add some ingredients to order
    and save your order in separate file 'customer_data.json'
    """

    def __init__(self, pizza=None):
        if not isinstance(pizza, General):
            raise TypeError("Wrong type of pizza")
        self.pizza = pizza

    def new_squad(self):
        print(self.pizza.extra_ingr)
        if str(input(f"If you want to add something, enter 'yes': ")) == 'yes':
            for ingr in self.pizza.extra_ingr:
                if input(f"If you want to add {ingr}, enter 'add': ") == 'add':
                    self.pizza.squad.append(ingr)
                    self.pizza.price += self.pizza.extra_ingr[ingr]

    def data_saving(self):
        data2 = {
            "person_name": self.pizza.person_name,
            "pizza_name": self.pizza.pizza_name,
            "value": self.pizza.price,
            "squad": self.pizza.squad
        }
        try:
            with open("customer_data.json", "w") as wrfile:
                json.dump(data2, wrfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 7")


n_day = int(datetime.datetime.today().weekday()) - 1
try:
    with open("data.json", "r") as rfile:
        data2 = json.load(rfile)
except FileNotFoundError:
            raise FileNotFoundError("Error 7")
menu = list(data2)
for i in range(len(menu)):
    if i == n_day:
        menu1 = menu[i]
days = [Pizza1, Pizza2, Pizza3, Pizza4, Pizza5, Pizza6, Pizza7]
obj = days[n_day]
name = str(input(f'What is your name? '))
res = obj(menu1["pizza_name"], menu1["value"], menu1["squad"], name, menu1["possible_extra_ingredients"])
order = Order(res)
order.new_squad()
order.data_saving()
try:
    with open("customer_data.json", "r") as rfile:
        data3 = json.load(rfile)
except FileNotFoundError:
            raise FileNotFoundError("Error 7")
print(dict(data3))

# try:
#     with open("data.json", "r") as rfile:
#         data3 = json.load(rfile)
# except FileNotFoundError:
#             raise FileNotFoundError("Error 7")
# print(dict(data3[2]))
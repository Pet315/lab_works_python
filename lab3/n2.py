import json
from datetime import datetime

data1 = [
    {
        "day": "Monday",
        "pizza_name": "Margaritta",
        "squad": ["tomato sauce", "mozzarella", "oregano"],
        "possible_extra_ingredients": ["pineapple", "mushrooms", "ham", "salami"],
        "ingredients_will_be_added": [],
        "possible_drinks": ["cola", "fanta", "sprite"],
        "selected_drink": '',
        "value": 100
    },
    {
        "day": "Tuesday",
        "pizza_name": "Carbonara",
        "squad": "Tomato sauce, mozzarella, parmesan, eggs, bacon",
        "possible_extra_ingredients": ["pesto", "olives", "capers"],
        "ingredients_will_be_added": [],
        "possible_drinks": ["cola", "fanta", "sprite"],
        "selected_drink": '',
        "value": 160
    },
    {
        "day": "Friday",
        "pizza_name": "Vegetariana",
        "squad": "Tomato sauce, mozzarella, basil",
        "possible_extra_ingredients": ["olives", "capers", "zucchini", "eggplant", "pepper"],
        "ingredients_will_be_added": [],
        "possible_drinks": ["cola", "fanta", "sprite"],
        "selected_drink": '',
        "value": 55
    }
]
with open("data.json", "w") as wrfile:
    json.dump(data1, wrfile)


class Day:
    """
    Class, that uses information about day to define, which type of pizza is
    the pizza-of-the-day now
    """

    def __init__(self, n_day):
        self.n_day = n_day

    def process(self):
        with open("data.json", "r") as rfile:
            data2 = json.load(rfile)
        menu = list(data2)
        for menu1 in menu:
            if menu1["day"] == self.n_day or menu1["pizza_name"] == self.n_day:
                return menu1
        raise Exception("There is no pizza-of-the-day for today")

class Order(Day):
    """
    Class, where customer is doing an order
    """

    def __init__(self, ingredients=[], drink='', day=datetime.today().strftime('%A')):
        super().__init__(day)
        self.ingredients = ingredients
        self.drink = drink

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        for mr in value:
            if not isinstance(mr, str):
                raise TypeError("Error 5")
        if len(value) < 0:
            raise IndexError("Error 6")
        self.__ingredients = list(value)

    @property
    def drink(self):
        return self.__drink

    @drink.setter
    def drink(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__drink = value

    def process(self):
        details = super().process()
        if len(self.ingredients):
            for i in range(len(self.ingredients)):
                for n_ing in details["possible_extra_ingredients"]:
                    if n_ing == self.ingredients[i]:
                        details["ingredients_will_be_added"].append(n_ing)
                        details["value"] = details["value"] + 10
        if len(self.drink):
            for n_dr in details["possible_drinks"]:
                if n_dr == self.drink:
                    details["selected_drink"] = self.drink
                    details["value"] = details["value"] + 25
        return f'PN: {details["pizza_name"]}, EI: {details["ingredients_will_be_added"]}, VL: {details["value"]}, DR: {details["selected_drink"]}'





class Order1(Order):
    """
    Class, that uses, when customer doesn't want a pizza-of-the-day
    and wants to make his own order
    """
    def __init__(self, pizza, ingredients=[], drink=''):
        super().__init__(ingredients, drink, pizza)

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, value):
        for pz in value:
            if not isinstance(pz, str):
                raise TypeError("Error 5")
        if len(value) < 0:
            raise IndexError("Error 6")
        self.__pizza = list(value)


print("Press 'stock' to choose pizza-of-the-day or something else to choose another pizza")
choice = input()
if choice=='stock':
    ord = Order(["pineapple", "capers"], "fanta")
    print(ord.process())
else:
    ord = Order1("Carbonara", ["ham", "olives"], "cola")
    print(ord.process())

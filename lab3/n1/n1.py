import json
from datetime import datetime

data1 = [
    {
        "unique_number": 1746,
        "price": 250,
        "event_date": "2021-11-26",
        "is_student": False
    },
    {
        "unique_number": 8309,
        "price": 250,
        "event_date": "2022-02-18",
        "is_student": False
    },
    {
        "unique_number": 9561,
        "price": 250,
        "event_date": "2021-12-21",
        "is_student": True
    }
]

try:
    with open("info.json", "w") as wrfile:
        json.dump(data1, wrfile)
except FileNotFoundError:
    raise FileNotFoundError("Error 7")

data2 = []
try:
    with open("tickets_list.json", "w") as wrfile:
        json.dump(data2, wrfile)
except FileNotFoundError:
    raise FileNotFoundError("Error 7")

class General:
    def __init__(self, unique_number, price, person_name, event_date):
        self.unique_number = unique_number
        self.price = price
        self.person_name = person_name
        self.event_date = event_date

        @property
        def unique_number(self):
            return self.__unique_number

        @unique_number.setter
        def unique_number(self, value):
            if not isinstance(value, int):
                raise TypeError("Error 1")
            if value < 0:
                raise ValueError("Error 2")
            self.__unique_number = value

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
        def person_name(self):
            return self.__person_name

        @person_name.setter
        def person_name(self, value):
            if not isinstance(value, str):
                raise TypeError("Error 3")
            if not value:
                raise ValueError("Error 4")
            self.__person_name = value

        @property
        def event_date(self):
            return self.__event_date

        @person_name.setter
        def event_date(self, value):
            if not isinstance(value, str):
                raise TypeError("Error 3")
            if not value:
                raise ValueError("Error 4")
            self.event_date = value


class Regular_Ticket(General):
    def __init__(self, unique_number, price, person_name, event_date):
        super().__init__(unique_number, price, person_name, event_date)

    def __str__(self):
        return f'Regular_Ticket: {self.unique_number}, {self.price}, {self.person_name}, {self.event_date}'

    def ticket_price(self):
        return self.price


class Advance_Ticket(General):
    def __init__(self, unique_number, price, person_name, event_date):
        super().__init__(unique_number, price, person_name, event_date)
        self.price = self.price*0.4

    def __str__(self):
        return f'Advance_Ticket: {self.unique_number}, {self.price}, {self.person_name}, {self.event_date}'

    def ticket_price(self):
        return self.price


class Student_Ticket(General):
    def __init__(self, unique_number, price, person_name, event_date):
        super().__init__(unique_number, price, person_name, event_date)
        self.price = self.price * 0.5

    def __str__(self):
        return f'Student_Ticket: {self.unique_number}, {self.price}, {self.person_name}, {self.event_date}'

    def ticket_price(self):
        return self.price


class Late_Ticket(General):
    def __init__(self, unique_number, price, person_name, event_date):
        super().__init__(unique_number, price, person_name, event_date)
        self.price = self.price * 1.1

    def __str__(self):
        return f'Late_Ticket: {self.unique_number}, {self.price}, {self.person_name}, {self.event_date}'

    def ticket_price(self):
        return self.price


class Order:
    """
    Class Order. It contains a possibility to add some ingredients to order
    and save your order in separate file 'customer_data.json'
    """

    def __init__(self, info=None):
        if not isinstance(info, General):
            raise TypeError("Error 6")
        self.info = info

    def data_saving(self):
        data2 = {
            "person_name": self.info.person_name,
            "unique_number": self.info.unique_number,
            "event_date": self.info.event_date,
            "price": self.info.price
        }
        try:
            with open("customer_data.json", "w") as wrfile:
                json.dump(data2, wrfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 7")
        try:
            with open("tickets_list.json", "r") as rfile:
                data4 = json.load(rfile)
                data4.append(data2)
        except FileNotFoundError:
            raise FileNotFoundError("Error 8")
        try:
            with open("tickets_list.json", "w") as wrfile:
                json.dump(data4, wrfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 7")

    def construct_by_number(self, un_n):
        try:
            with open("tickets_list.json", "r") as rfile:
                data4 = json.load(rfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 8")
        for elem in data4:
            if un_n == elem["unique_number"]:
                return elem
        return f'Please, check your unique number'


def process(i=0):
    if not isinstance(i, int):
        raise TypeError("Error 10")
    try:
        with open("info.json", "r") as rfile:
            data2 = json.load(rfile)
            ticket = data2[i]
    except FileNotFoundError:
        raise FileNotFoundError("Error 8")
    time_left = (datetime.strptime(ticket["event_date"], '%Y-%m-%d') - datetime.now()).days
    # print(time_left)
    types = [Regular_Ticket, Advance_Ticket, Student_Ticket, Late_Ticket]
    if ticket["is_student"]:
        obj = types[2]
    elif time_left > 60:
        obj = types[1]
    elif time_left < 10:
        obj = types[3]
    else:
        obj = types[0]
    name = str(input(f'What is your name? '))
    res = obj(ticket["unique_number"], ticket["price"], name, ticket["event_date"])
    return Order(res)


for i in range(3):
    process(i).data_saving()

try:
    with open("customer_data.json", "r") as rfile:
        data3 = json.load(rfile)
except FileNotFoundError:
            raise FileNotFoundError("Error 8")
print(dict(data3))

x1 = Order(Student_Ticket(4356, 250, "Sam", "2022-03-25"))
print(x1.construct_by_number(8309))

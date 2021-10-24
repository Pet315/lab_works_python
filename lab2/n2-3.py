class Student:
    """Class Student"""

    def __init__(self, surname, name, book_numb, marks):
        self.surname = surname
        self.name = name
        self.book_numb = book_numb
        self.marks = marks

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
    def book_numb(self):
        return self.__book_numb

    @book_numb.setter
    def book_numb(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Error 1")
        if value < 0:
            raise ValueError("Error 2")
        self.__book_numb = value

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        for mr in value:
            if not isinstance(mr, (int, float)):
                raise TypeError("Error 5")
            if mr < 0 or mr > 15:
                raise ValueError("Error 6")
        self.__marks = list(value)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f'sr: {self.surname}, nm: {self.name}, bn: {self.book_numb}, mr: {self.marks}'

    def __lt__(self, other):
        return self.average() > other.average()


class Group:
    """Class Group"""

    def __init__(self, st_group):
        if not all([isinstance(person, Student) for person in st_group]):
            raise TypeError("Error 7")
        if len(st_group) < 0 or len(st_group) > 20:
            raise ValueError("Error 8")
        self.info = []
        if not all([self.process(person) for person in st_group]):
            raise ValueError("Error 9")
        self.st_group = st_group

    def add(self, person):
        if not isinstance(person, Student):
            raise TypeError("Error 10")
        if not self.process(person):
            raise ValueError("Error 11")
        self.st_group.append(person)

    def delete(self, person):
        if not isinstance(person, Student):
            raise TypeError("Error 12")
        self.st_group.remove(person)

    def process(self, person):
        pr = person.surname + person.name
        if pr in self.info:
            return False
        else:
            self.info.append(pr)
        return True

    def best5(self):
        self.st_group = sorted(self.st_group)
        elite = [
            f'N: {self.st_group[i].name}, S: {self.st_group[i].surname}, B: {self.st_group[i].book_numb}, A: {self.st_group[i].average()}'
            for i in range(5)]
        return elite[:5]


st1 = Student("dtshyt", "ytdthrg", 25653, [1, 7, 12, 11])
st2 = Student("fjytj", "resythyt", 35634, [8, 9, 14, 6])
st3 = Student("rtjyu", "fjghcf", 78665, [10, 12, 5, 7])
st4 = Student("utgjcn", "hfgutydr", 64525, [10, 12, 6, 8])
st5 = Student("eyttsr", "rthjytj", 765, [15, 12, 13, 4])
st6 = Student("ndghffgs", "tyedh", 9945, [14, 12, 9, 5])
Group = Group([st1, st2, st3, st4, st5, st6])
print(Group.best5())

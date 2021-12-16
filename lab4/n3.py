import json
from abc import ABC, abstractmethod


class ICourse(ABC):
    @abstractmethod
    def __init__(self, name, teacher, program):
        pass


class ILocalCourse(ABC):
    @abstractmethod
    def __init__(self, name, teacher, program):
        pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def __init__(self, name, teacher, program):
        pass


class ITeacher(ABC):
    @abstractmethod
    def __init__(self, t_name, c_name):
        pass


class ICourseFactory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def t_add(self, t_name, course):
        pass

    @abstractmethod
    def c_add(self, name, teacher, program, type_course):
        pass


class Course(ICourse):
    def __init__(self, name, teacher, program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, values):
        if not all([isinstance(nm, str) for nm in values]):
            raise TypeError("Error 1")
        if not values:
            raise ValueError("Error 2")
        self.__name = values

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, str):
            raise TypeError("Error 3")
        if not teacher:
            raise ValueError("Error 4")
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, values):
        if not all([isinstance(pg, str) for pg in values]):
            raise TypeError("Error 1")
        if not values:
            raise ValueError("Error 2")
        self.__program = values


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)


class Teacher(ITeacher):
    def __init__(self, t_name, c_name):
        self.t_name = t_name
        self.c_name = c_name

    @property
    def t_name(self):
        return self.__t_name

    @t_name.setter
    def t_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Error 3")
        if not value:
            raise ValueError("Error 4")
        self.__t_name = value

    @property
    def c_name(self):
        return self.__c_name

    @c_name.setter
    def c_name(self, values):
        if not all([isinstance(course, str) for course in values]):
            raise TypeError("Error 1")
        if not values:
            raise ValueError("Error 2")
        self.__c_name = values


class CourseFactory(ICourseFactory):
    def __init__(self):
        self.t_dict = {}
        self.c_dict = {}

    def t_add(self, t_name, c_subjects):
        if not c_subjects:
            raise ValueError("Error 5")
        self.t_dict.update({t_name: Teacher(t_name, c_subjects).__dict__})
        try:
            with open('case1.json', 'w') as wrfile:
                json.dump(self.t_dict, wrfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 6")
        return Teacher(t_name, c_subjects)

    def c_add(self, name_surname, t_code, program, c_type):
        dict_of_courses = {'Local': LocalCourse(name_surname, t_code.t_name, program),
                           'Offsite': OffsiteCourse(name_surname, t_code.t_name, program)}
        if name_surname not in t_code.c_name:
            t_code.c_name.append(name_surname)
        self.t_add(t_code.t_name, t_code.c_name)
        self.c_dict.update({name_surname: dict_of_courses[c_type].__dict__})
        try:
            with open('case2.json', 'w') as wrfile:
                json.dump(self.c_dict, wrfile)
        except FileNotFoundError:
            raise FileNotFoundError("Error 6")
        return dict_of_courses[c_type]


a = CourseFactory()
x1 = a.t_add('John Smitt', ['Chemistry', 'Biology', 'Physics', 'Math'])
x2 = a.t_add('Viktor Mitlov', ['Higher mathematics', 'Physics', 'Electrical engineering'])
y1 = a.c_add('Biology', x1, ['mitosis', 'meiosis', 'virusology', 'zoology'], 'Offsite')
y2 = a.c_add('Physics', x2, ['mechanics', 'dynamics', 'electrostatics'], 'Local')

print("Who will teach:")
for m, n in a.t_dict.items():
    print(f'{m}, {n}')

print("--\nWhat courses are:")
for m1, n1 in a.c_dict.items():
    print(f'{m1}, {n1}')

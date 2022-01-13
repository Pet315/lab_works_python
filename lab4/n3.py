from abc import ABC, abstractmethod
import mysql.connector
from DatabaseInfo import DatabaseInfo


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
    def c_add(self, type_course, name, teacher, program):
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
        cnx = mysql.connector.connect(user=DatabaseInfo.user, password=DatabaseInfo.password,
                                      host=DatabaseInfo.host, database=DatabaseInfo.database,
                                      auth_plugin=DatabaseInfo.auth_plugin)
        id = 0
        for sub in c_subjects:
            data = (id, t_name, sub)
            s = 'INSERT academy.teacher VALUES (%s, %s, %s);'
            cursor = cnx.cursor()
            cursor.execute(s, data)
        cnx.commit()
        cnx.close()
        return Teacher(t_name, c_subjects)

    def c_add(self, c_type, name, t_code, topics):
        types = {'Local': LocalCourse(name, t_code.t_name, topics),
                 'Offsite': OffsiteCourse(name, t_code.t_name, topics)}
        if name not in t_code.c_name:
            t_code.c_name.append(name)
        self.c_dict.update({name: types[c_type].__dict__})
        id_course = 0
        for topic in topics:
            cnx = mysql.connector.connect(user=DatabaseInfo.user, password=DatabaseInfo.password,
                                          host=DatabaseInfo.host, database=DatabaseInfo.database,
                                          auth_plugin=DatabaseInfo.auth_plugin)
            id_t = "\'" + t_code.t_name + "\'"
            s1 = "SELECT id_teacher FROM academy.teacher WHERE name_surname = " + id_t + ';'
            cursor = cnx.cursor()
            cursor.execute(s1)
            id_teacher = cursor.fetchone()[0]
            # print(id_teacher)
            cnx.close()
            cnx = mysql.connector.connect(user=DatabaseInfo.user, password=DatabaseInfo.password,
                                          host=DatabaseInfo.host, database=DatabaseInfo.database,
                                          auth_plugin=DatabaseInfo.auth_plugin)
            data = (id_course, c_type, name, id_teacher, topic)
            # print(f'{data}\n')
            id_course += 1
            s2 = 'INSERT academy.course VALUES (%s, %s, %s, %s, %s);'
            cursor = cnx.cursor()
            cursor.execute(s2, data)
            cnx.close()
        return types[c_type]


if __name__ == "__main__":
    a = CourseFactory()
    x1 = a.t_add('John Smitt', ['Chemistry', 'Biology', 'Physics', 'Math'])
    x2 = a.t_add('Viktor Mitlov', ['Higher mathematics', 'Physics', 'Electrical engineering'])
    y1 = a.c_add('Offsite', 'Biology', x1, ['mitosis', 'meiosis', 'virusology', 'zoology'])
    y2 = a.c_add('Local', 'Physics', x2, ['mechanics', 'dynamics', 'electrostatics'])

    print("Who will teach:")
    for m, n in a.t_dict.items():
        print(f'{m}, {n}')

    print("--\nWhat courses are:")
    for m1, n1 in a.c_dict.items():
        print(f'{m1}, {n1}')

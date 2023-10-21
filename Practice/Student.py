"""
Класс студент нужен для анализа успеваемости учеников с системе оценки образования для школ

Данные вводимые в класс:
ФИО
Группа
Оценка
Отсутвия

Операции реализованные в классе:
Создать группу
Удалить группу
Добавить студента в группуу
Удалить студента из группы
Проставить оценнку
Убрать оценку
Поставить прогул

Средний балл студента
Средний балл в группе

Количество прогулов студента
Количество прогулов в группе

Показать список имён в группе
Подсчитать количество учеников в группе
Подсчитать количество учеников в школе

Показать самую успевающую группу
Показать самую отстающую группу

создаются списки и уже геттерами и сеттерами если надо добавляем
в них

Иниуиируем класс с первой группы, во всём остальном
"""


class Student:

    __MIN = 1
    __MAX = 5

    def __init__(self, school_name):

        self.__school_name = school_name
        self.__school = {self.__school_name: {}}

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __eq__(self, other):
        pass

    def add_group(self, name):
        pass

    def del_group(self, name):
        pass

    def add_student(self, name):
        pass

    def del_student(self, name):
        pass

    #  -1 это прогулы
    def add_mark(self, name):
        pass

    def del_mark(self, name):
        pass

    def avg_marks_stud(self, name):
        pass

    def avg_marks_group(self, name):
        pass

    def avg_marks_school(self, name):
        pass

    def absence_student(self, name):
        pass

    def absence_group(self, name):
        pass

    def absence_school(self, name):
        pass

    def group_list(self, name):
        pass

    def school_len(self, name):
        pass

    def group_len(self, name):
        pass

    def successful_group(self):
        pass

    def unsuccessful_group(self):
        pass


s = Student('Group_1')
print(s.__dict__)

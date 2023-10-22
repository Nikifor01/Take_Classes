class Student:
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
        self.__school[name] = {}

    def del_group(self, name):
        del self.__school[name]

    def add_student(self, group, name):
        self.__school[group][name] = []

    def del_student(self, group, name):
        del self.__school[group][name]

    #  -1 это прогулы
    def add_mark(self, group, name, mark):
        self.__school[group][name].append(mark)

    def del_mark(self, group, name, mark):
        self.__school[group][name].remove(mark)

    def avg_marks_stud(self, group, name):
        return sum(self.__school[group][name]) / len(self.__school[group][name])

    def avg_marks_group(self, group, avg_type='each'):
        marks = 0
        #  НАУЧИТЬ СОПРОТИВЛЯТЬСЯ НОЛЯМ
        if avg_type == 'each':
            for i in self.__school[group].values():
                marks += sum(i) / len(i)

            return marks / len(self.__school[group])

        elif avg_type == 'total':
            return sum([a for c in self.__school[group].values() for a in c]) / len(
                [a for c in self.__school[group].values() for a in c])

    def avg_marks_school(self, avg_type='total'):
        #  НАУЧИТЬ СОПРОТИВЛЯТЬСЯ НОЛЯМ
        a = []

        if avg_type == 'total':
            for i in self.__school.values():
                for j in i.values():
                    a.extend(j)

            return sum(a) / len(a)

    def absence_student(self, group, name):
        count = 0

        for i in self.__school[group][name]:
            if i == -1:
                count += 1

        return count

    def absence_group(self, group):
        count = 0

        for i in self.__school[group].values():
            if -1 in i:
                count += 1

        return count

    def absence_school(self):
        count = 0

        for i in self.__school.values():
            for j in i.values():
                for k in j:
                    if k == -1:
                        count += 1

        return count

    def group_list(self, group):
        return self.__school[group].keys()

    def group_len(self, group):
        return len(self.__school[group].keys())

    def school_list(self):
        names = []
        for i in self.__school.values():
            for j in i.keys():
                names.append(j)

        return names

    def school_len(self):
        count = 0

        for i in self.__school.values():
            count += len(i)

        return count

    def successful_group(self):
        max_avg = 0
        best_group = ""

        for group, students in self.__school.items():
            avg = self.avg_marks_group(group)
            if avg > max_avg:
                max_avg = avg
                best_group = group

        return best_group, max_avg

    def unsuccessful_group(self):
        min_avg = float('inf')
        worst_group = ""

        for group, students in self.__school.items():
            avg = self.avg_marks_group(group)
            if avg < min_avg:
                min_avg = avg
                worst_group = group

        return worst_group, min_avg


s = Student('Group_1')
s.add_group('Group_2')
s.del_group('Group_2')
print(s.__dict__)

s.add_student('Group_1', 'Oleg Vitalievich Tch')
s.add_student('Group_1', 'Olga Vitalievna Tch')
print(s.__dict__)

s.add_mark('Group_1', 'Oleg Vitalievich Tch', 5)
s.add_mark('Group_1', 'Oleg Vitalievich Tch', 2)
s.add_mark('Group_1', 'Olga Vitalievna Tch', 5)
s.add_mark('Group_1', 'Olga Vitalievna Tch', 4)
s.add_mark('Group_1', 'Olga Vitalievna Tch', 3)
print(s.__dict__)

print(s.avg_marks_stud('Group_1', 'Oleg Vitalievich Tch'))
print(s.avg_marks_group('Group_1'))
print(s.avg_marks_group('Group_1', 'total'))
s.add_group('Group_2')
s.add_group('Group_3')
print(s.__dict__)

s.add_student('Group_1', 'Alice Vitalievich Tch')
s.add_student('Group_2', 'Mike Vitalievich Tch')
s.add_student('Group_3', 'Lera Vitalievna Tch')
s.add_student('Group_3', 'Anna Vitalievna Tch')
s.add_student('Group_2', 'Olga Vitalievna Th')

s.add_mark('Group_1', 'Alice Vitalievich Tch', 4)
s.add_mark('Group_2', 'Mike Vitalievich Tch', 3)
s.add_mark('Group_3', 'Lera Vitalievna Tch', 3)
s.add_mark('Group_3', 'Anna Vitalievna Tch', 5)
s.add_mark('Group_2', 'Olga Vitalievna Th', 2)
s.add_mark('Group_1', 'Alice Vitalievich Tch', 3)
s.add_mark('Group_2', 'Mike Vitalievich Tch', 2)
s.add_mark('Group_3', 'Lera Vitalievna Tch', 1)
s.add_mark('Group_3', 'Anna Vitalievna Tch', 5)
s.add_mark('Group_2', 'Olga Vitalievna Th', 4)
s.add_mark('Group_1', 'Alice Vitalievich Tch', 5)
s.add_mark('Group_2', 'Mike Vitalievich Tch', 4)
s.add_mark('Group_3', 'Lera Vitalievna Tch', 3)
s.add_mark('Group_3', 'Anna Vitalievna Tch', 2)
s.add_mark('Group_2', 'Olga Vitalievna Th', 1)
print(s.__dict__)

print(s.avg_marks_school())

print(s.group_list('Group_3'))

print(s.group_len('Group_3'))

print(s.school_list())

print(s.school_len())

s.add_mark('Group_1', 'Oleg Vitalievich Tch', -1)
s.add_mark('Group_1', 'Oleg Vitalievich Tch', -1)
s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
s.add_mark('Group_3', 'Anna Vitalievna Tch', -1)
print(s.__dict__)

print(s.absence_student('Group_1', 'Olga Vitalievna Tch'))
print(s.__dict__)

print(s.absence_group('Group_3'))

print(s.absence_school())

print(s.successful_group())

print(s.avg_marks_group('Group_1'))
print(s.avg_marks_group('Group_2'))
print(s.avg_marks_group('Group_3'))

print(s.unsuccessful_group())

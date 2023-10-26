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


    создать геттеры для просмотра


    Иниуиируем класс с первой пустой группы


    Проверки:
    Имя должно состаять из трёх частей и только букв
    Оценка от одного до пяти включительно
    Прогул это всегда -1
    Не допустить деления на ноль



    """

    __MIN = 1
    __MAX = 5

    def __init__(self, school_name, group):

        self.__school_name = school_name
        self.__group = group
        self.__school = {self.__group: {}}

    def __call__(self, *args, **kwargs):
        return print('You are creating new school, group one successfully uploaded')

    def __str__(self):
        return f'{self.__class__} : {self.__school}'

    def __repr__(self):
        return f'{self.__class__} : {self.__school_name}'

    def __len__(self):
        return len(self.__school)

    def __eq__(self, other):
        return len(self.__school) == len(other.__school)

    def __lt__(self, other):
        return len(self.__school) < len(other.__school)

    def __gt__(self, other):
        return len(self.__school) > len(other.__school)

    def __le__(self, other):
        return len(self.__school) <= len(other.__school)

    def __ge__(self, other):
        return len(self.__school) >= len(other.__school)

    def __hash__(self):
        return hash((self.__school_name, self.__group))

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def add_group(self, name):
        if not self._group_valid(name):
            raise ValueError('It must be text')
        self.__school[name] = {}

    def del_group(self, name):
        del self.__school[name]

    def add_student(self, group, name):
        if not self._name_valid(name):
            raise ValueError('It must be full name like in ID')
        self.__school[group][name] = []

    def del_student(self, group, name):
        del self.__school[group][name]

    #  -1 это прогулы
    def add_mark(self, group, name, mark):
        if self.__marks_valid(mark):
            self.__school[group][name].append(mark)
        else:
            raise ValueError('It ,ust be from 1 to 5 or -1 for absence')

    def del_mark(self, group, name, mark):
        self.__school[group][name].remove(mark)

    def get_mark(self, group, name):
        return self.__school[group][name]

    def avg_marks_stud(self, group, name):
        return sum(self.__school[group][name]) / len(self.__school[group][name])

    def avg_marks_group(self, group, avg_type='each'):
        marks = 0
        #  НАУЧИТЬ СОПРОТИВЛЯТЬСЯ НОЛЯМ
        if self.__school[group].values() != 0:
            if avg_type == 'each':
                for i in self.__school[group].values():
                    marks += sum(i) / len(i)

                return marks / len(self.__school[group])

            elif avg_type == 'total':
                val = len(
                    [a for c in self.__school[group].values() for a in c])
                if val == 0:
                    raise ZeroDivisionError
                else:
                    return sum([a for c in self.__school[group].values() for a in c]) / len(
                        [a for c in self.__school[group].values() for a in c])
        else:
            raise ZeroDivisionError

    def avg_marks_school(self, avg_type='total'):
        #  НАУЧИТЬ СОПРОТИВЛЯТЬСЯ НОЛЯМ
        a = []

        if avg_type == 'total':
            for i in self.__school.values():
                for j in i.values():
                    a.extend(j)

            if len(a) != 0:
                return sum(a) / len(a)
            else:
                raise ZeroDivisionError

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

    @classmethod
    def __marks_valid(cls, mark):
        return (cls.__MIN <= mark <= cls.__MAX) or (mark == -1)

    @staticmethod
    def _group_valid(name):
        return isinstance(name, str)

    @staticmethod
    def _name_valid(name):
        return len(name.split()) == 3 and (isinstance(name, str))

    # @property
    # def groups(self):
    #     return self.__school.keys()
    #
    # @groups.setter
    # def groups(self, name):
    #     self.__school[name] = {}
    #
    # @groups.deleter
    # def groups(self, name):
    #     del self.__school[name]


s = Student('School_1', 'Group_1')
s1 = Student('School_2', 'Group_1')

s1.add_group('Group_2')

print(s1.__dict__)

s1.add_student('Group_1', 'O O O')
s1.add_student('Group_2', 'O i O')

print(s1.__dict__)
#print(s1.avg_marks_school())
s1.add_mark('Group_1', 'O O O', 3)
s1.add_mark('Group_1', 'O O O', -1)
s1.add_mark('Group_2', 'O i O', 3)
s1.add_mark('Group_2', 'O i O', -1)
print(s1.__dict__)

print(s1.avg_marks_group('Group_1', 'total'))
print(s1.avg_marks_school())

sl = s1.get_mark('Group_1', 'O O O')
print(sl[0])

# s1.add_student('Group_1', 'O O')
# print(s1.__dict__)

# s1.add_mark('Group_1', 'O O O', 6)
# print(s1.__dict__)

# print(s == s1)
# print(s > s1)
# print(s < s1)
# print(s >= s1)
# print(s <= s1)
#
# print(hash(s), hash(s1), sep='\n')
# print(s.__dict__)
# print(s1.__dict__)


# s()
# len(s)
# print(s)

# s.add_group('Group_2')
# s.del_group('Group_2')
# print(s.__dict__)
#
# s.add_student('Group_1', 'Oleg Vitalievich Tch')
# s.add_student('Group_1', 'Olga Vitalievna Tch')
# print(s.__dict__)
#
# s.add_mark('Group_1', 'Oleg Vitalievich Tch', 5)
# s.add_mark('Group_1', 'Oleg Vitalievich Tch', 2)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', 5)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', 4)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', 3)
# print(s.__dict__)
#
# print(s.avg_marks_stud('Group_1', 'Oleg Vitalievich Tch'))
# print(s.avg_marks_group('Group_1'))
# print(s.avg_marks_group('Group_1', 'total'))
# s.add_group('Group_2')
# s.add_group('Group_3')
# print(s.__dict__)
#
# s.add_student('Group_1', 'Alice Vitalievich Tch')
# s.add_student('Group_2', 'Mike Vitalievich Tch')
# s.add_student('Group_3', 'Lera Vitalievna Tch')
# s.add_student('Group_3', 'Anna Vitalievna Tch')
# s.add_student('Group_2', 'Olga Vitalievna Th')
#
# s.add_mark('Group_1', 'Alice Vitalievich Tch', 4)
# s.add_mark('Group_2', 'Mike Vitalievich Tch', 3)
# s.add_mark('Group_3', 'Lera Vitalievna Tch', 3)
# s.add_mark('Group_3', 'Anna Vitalievna Tch', 5)
# s.add_mark('Group_2', 'Olga Vitalievna Th', 2)
# s.add_mark('Group_1', 'Alice Vitalievich Tch', 3)
# s.add_mark('Group_2', 'Mike Vitalievich Tch', 2)
# s.add_mark('Group_3', 'Lera Vitalievna Tch', 1)
# s.add_mark('Group_3', 'Anna Vitalievna Tch', 5)
# s.add_mark('Group_2', 'Olga Vitalievna Th', 4)
# s.add_mark('Group_1', 'Alice Vitalievich Tch', 5)
# s.add_mark('Group_2', 'Mike Vitalievich Tch', 4)
# s.add_mark('Group_3', 'Lera Vitalievna Tch', 3)
# s.add_mark('Group_3', 'Anna Vitalievna Tch', 2)
# s.add_mark('Group_2', 'Olga Vitalievna Th', 1)
# print(s.__dict__)
#
# print(s.avg_marks_school())
#
# print(s.group_list('Group_3'))
#
# print(s.group_len('Group_3'))
#
# print(s.school_list())
#
# print(s.school_len())
#
# s.add_mark('Group_1', 'Oleg Vitalievich Tch', -1)
# s.add_mark('Group_1', 'Oleg Vitalievich Tch', -1)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
# s.add_mark('Group_1', 'Olga Vitalievna Tch', -1)
# s.add_mark('Group_3', 'Anna Vitalievna Tch', -1)
# print(s.__dict__)
#
# print(s.absence_student('Group_1', 'Olga Vitalievna Tch'))
# print(s.__dict__)
#
# print(s.absence_group('Group_3'))
#
# print(s.absence_school())
#
# print(s.successful_group())
#
# print(s.avg_marks_group('Group_1'))
# print(s.avg_marks_group('Group_2'))
# print(s.avg_marks_group('Group_3'))
#
# print(s.unsuccessful_group())

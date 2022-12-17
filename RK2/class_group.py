# Вариант 28 А Печуркин Д.С. ИУ5Ц-51Б RK1

from operator import itemgetter


class Stud_Group:
    """Студенческая группа"""

    def __init__(self, id, name, count_students, dep_id):
        self.id = id
        self.name = name
        self.students = count_students
        self.dep_id = dep_id


class Departament:
    """Кафедра"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Merge:
    """
    Студенческие группы кафедр
    для реализации связи многие-ко-многим
    """

    def __init__(self, dep_id, stud_id):
        self.dep_id = dep_id
        self.stud_id = stud_id


Stud_Groups = [
    Stud_Group(1, 'ИУ5Ц-51Б', 3, 1),
    Stud_Group(2, 'РК6-30', 10, 4),
    Stud_Group(3, 'ИБМ2-61', 6, 5),
    Stud_Group(4, 'ИБМ2-62', 6, 5),
    Stud_Group(5, 'МТ8-31', 8, 3),
    Stud_Group(6, 'ИУ3-31', 11, 2),
    Stud_Group(7, 'ИУ3-32', 11, 2),
    Stud_Group(8, 'ИУ5Ц-52Б', 5, 1),
    Stud_Group(9, 'ИУ5Ц-53Б', 7, 1),
]

Departaments = [
    Departament(1, 'ИУ5 - Системы обработки информации и управления'),
    Departament(2, 'ИУ3 - Информационные системы и телекоммуникации'),
    Departament(3, 'МТ8 - Материаловедение'),
    Departament(4, 'РК6 - Системы автоматизированного проектирования', ),
    Departament(5, 'ИБМ2 - Экономика и организация производства'),
]

Merges = [
    Merge(1, 1),
    Merge(1, 8),
    Merge(1, 9),
    Merge(3, 5),
    Merge(5, 3),
    Merge(5, 4),
    Merge(2, 6),
    Merge(2, 7),
]

def exercise_G1(Stud_Groups, Departaments):
    # Соединение данных один-ко-многим
    one_to_many = [(group.name, group.students, dep.name)
                   for dep in Departaments
                   for group in Stud_Groups
                   if dep.id == group.dep_id]
    res_0 = sorted(one_to_many, key=itemgetter(2))
    return res_0

def exercise_G2(Departaments, one_to_many):
    res_1 = []

    for dep in Departaments:
        # Список студентов кафедры
        deps = list(filter(lambda i: i[2] == dep.name, one_to_many))
        # Если кафедра не пустая
        if len(deps) > 0:
            # Кол-во студентов и суммарно студентов на кафедре
            stud_sum = sum([count for _, count, _ in deps])
            res_1.append((dep.name, stud_sum))
    # Сортировка по количеству по убыванию
    res_1 = sorted(res_1, key=itemgetter(1), reverse=True)
    return res_1

def exercise_G3(Stud_Groups, Departaments, Merges):
    res_2 = {}

    many_to_many_temp = [(dep.name, merge.dep_id, merge.stud_id)
                         for dep in Departaments
                         for merge in Merges
                         if dep.id == merge.dep_id]

    many_to_many = [(stud.name, stud.students, name)
                    for name, dep_id, stud_id in many_to_many_temp
                    for stud in Stud_Groups if stud.id == stud_id]

    # Перебираем все кафедры
    for dep in Departaments:
        if 'ИУ' in dep.name:
            # Список студентов кафедры
            list_studs = list(filter(lambda x: x[2] == dep.name, many_to_many))
            # Только названия кафедр
            list_deps = [name for name, _, _ in list_studs]
            # Добавляем результат в словарь
            # ключ - кафедра, значение - список групп
            res_2[dep.name] = list_deps

    return res_2

def main():
    # print('Вариант 28А Печуркин Д.С. ИУ5Ц-51Б\n')
    one_to_many = exercise_G1(Stud_Groups, Departaments)
    print("Задание 1")
    print(one_to_many)

    res_1 = exercise_G2(Departaments, one_to_many)
    print("Задание 2")
    print(res_1)


    res_2 = exercise_G3(Stud_Groups, Departaments, Merges)
    print("Задание 3")
    print(res_2)


if __name__ == '__main__':
    main()



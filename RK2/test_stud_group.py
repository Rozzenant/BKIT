import unittest

from class_group import Stud_Group, Merge, Departament, exercise_G1, exercise_G2, exercise_G3

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

one_to_many = exercise_G1(Stud_Groups, Departaments)

class test_Departament(unittest.TestCase):
    def test_class_Stud_Group_meaning(self):
        test_class_Stud_Group = Stud_Group(5, 'МТ8-31', 8, 3)
        self.assertEqual(test_class_Stud_Group.id, 5)
        self.assertEqual(test_class_Stud_Group.name, 'МТ8-31')
        self.assertEqual(test_class_Stud_Group.students, 8)
        self.assertEqual(test_class_Stud_Group.dep_id, 3)

    def test_class_Departament_zero_parameters(self):
        with self.assertRaises(TypeError) as context:
            Departament()
        self.assertEqual(
            "Departament.__init__() missing 2 required positional arguments: 'id' and 'name'",
            str(context.exception)
        )

    def test_class_Departament_zero_meaning(self):
        test_class_Departament = Departament(None, None)
        self.assertEqual(test_class_Departament.id, None)
        self.assertEqual(test_class_Departament.name, None)

    def test_class_Departament_meaning(self):
        test_class_Departament = Departament(2, 'ИБМ2 - Экономика и организация производства')
        self.assertEqual(test_class_Departament.id, 2)
        self.assertEqual(test_class_Departament.name, 'ИБМ2 - Экономика и организация производства')

    def test_class_Merge_meaning(self):
        test_class_sections_documents = Merge(5, 7)
        self.assertEqual(test_class_sections_documents.dep_id, 5)
        self.assertEqual(test_class_sections_documents.stud_id, 7)

    # Тестирование задания 1
    def test_task_1(self):
        self.assertEqual(exercise_G1(Stud_Groups, Departaments),
                         [('ИБМ2-61', 6, 'ИБМ2 - Экономика и организация производства'),
                          ('ИБМ2-62', 6, 'ИБМ2 - Экономика и организация производства'),
                          ('ИУ3-31', 11, 'ИУ3 - Информационные системы и телекоммуникации'),
                          ('ИУ3-32', 11, 'ИУ3 - Информационные системы и телекоммуникации'),
                          ('ИУ5Ц-51Б', 3, 'ИУ5 - Системы обработки информации и управления'),
                          ('ИУ5Ц-52Б', 5, 'ИУ5 - Системы обработки информации и управления'),
                          ('ИУ5Ц-53Б', 7, 'ИУ5 - Системы обработки информации и управления'),
                          ('МТ8-31', 8, 'МТ8 - Материаловедение'),
                          ('РК6-30', 10, 'РК6 - Системы автоматизированного проектирования')])
    # Тестирование задания 2
    def test_task_2(self):
        self.assertEqual(exercise_G2(Departaments, one_to_many),
                        [('ИУ3 - Информационные системы и телекоммуникации', 22),
                         ('ИУ5 - Системы обработки информации и управления', 15),
                         ('ИБМ2 - Экономика и организация производства', 12),
                         ('РК6 - Системы автоматизированного проектирования', 10),
                         ('МТ8 - Материаловедение', 8)])

    # Тестирование задания 3
    def test_task_3(self):
        self.assertEqual(exercise_G3(Stud_Groups, Departaments, Merges),
                         {'ИУ5 - Системы обработки информации и управления': ['ИУ5Ц-51Б', 'ИУ5Ц-52Б', 'ИУ5Ц-53Б'],
                          'ИУ3 - Информационные системы и телекоммуникации': ['ИУ3-31', 'ИУ3-32']})

if __name__ == '__main__':
    unittest.main()



import sys
import unittest
from unittest.mock import Mock, patch


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        # Проверяем на число
        while True:
            try:
                # Вводим с клавиатуры
                print(prompt, end="")
                coef_str = input()
                # Переводим строку в действительное число
                coef = float(coef_str)
            except:
                print("Введите число!")
            else:
                break

    return coef

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        result[float]: Список корней
    '''

    preresult = []
    result = set()
    D = b*b - 4*a*c

    if D == 0:
        preresult.append(-b/2*a)

    elif D > 0:
        root1 = (-b - D**0.5) / (2 * a)
        root2 = (-b + D**0.5) / (2 * a)

        if root1 >= 0:
            preresult.append(root1)
        if root2 >= 0:
            preresult.append(root2)

    for root in preresult:
        result.add(root ** 0.5)
        result.add(-root ** 0.5)

    return result


def main():
    """
    Основная фунция
    """

    a = get_coef(1, "Введите а: ")

    if not a:
        print("Это не биквадратное уравнение!")
        return

    b = get_coef(2, "Введите b: ")
    c = get_coef(3, "Введите с: ")

    roots = list(get_roots(a, b, c))

    len_roots = len(roots)

    if len_roots == 0:
        print("Корней нет")

    if len_roots == 1:
        print(f"Единственный корень: {roots[0]}")

    if len_roots == 2:
        print(f"Есть два корня: {roots[0]} и {roots[1]}")

    if len_roots == 3:
        print(f"Есть три корня: {roots[0]}, {roots[1]} и {roots[2]}")

    if len_roots == 4:
        print(f"Есть четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}")

class get_roots_TDD(unittest.TestCase):
    def test(self):
        self.assertEqual(get_roots(1, -4, 0), set())


        self.assertEqual(get_roots(1, -5, 6), {1.4142135623730951,
                                               -1.7320508075688772,
                                               1.7320508075688772,
                                               -1.4142135623730951})

        self.assertEqual(get_roots(-4, 16, 0), {0, 2, -2})
        self.assertRaises(TypeError, get_roots, 1 + 1j, 2 - 3j, 5 + 10j)

        # С Mock - объектами

        roots_obj = Roots4()
        roots_obj.roots = Mock(return_value=[5, 1, 8])

        print(roots_obj.roots(-4, 16, 0))

        roots_obj.roots.assert_called_once()
        roots_obj.roots.assert_called_with(-4, 16, 0)

        self.assertEqual(roots_obj.roots(1, 2, 3), set())

class Roots4:
    def __init__(self):
        pass

    def roots(self, a, b, c):
        return get_roots(a, b, c)

if __name__ == '__main__':
    unittest.main()
    # main()


from lab_python_oop.geometric_shape import Geometric_shape
from lab_python_oop.color import Color
from math import pi

class Circle(Geometric_shape):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"
    def __init__(self, color, radius):
        self.radius = radius
        self.color = Color()
        self.color = color

    def square(self):
        return pi * self.radius ** 2

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета радиуса {} и площадью {}.'.format(
            Circle.get_figure_type(),
            self.color,
            self.radius,
            self.square()
        )
from lab_python_oop.geometric_shape import Geometric_shape
from lab_python_oop.color import Color

class Rectangle(Geometric_shape):
    """
    Класс «Прямоугольник» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Прямоугольник"
    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        self.color = Color()
        self.color = color

    def square(self):
        return self.width * self.height

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.color,
            self.width,
            self.height,
            self.square()
        )
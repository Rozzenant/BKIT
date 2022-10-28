from lab_python_oop.rectangle import Rectangle

class Box(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Квадрат"
    def __init__(self, color, width):
        super().__init__(color, width, width)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return '{} {} цвета длиной {} площадью {}.'.format(
            Box.get_figure_type(),
            self.color,
            self.width,
            self.square()
        )
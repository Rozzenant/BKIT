from abc import ABC, abstractmethod


class Geometric_shape(ABC):
    """
    Класс «Геометрическая фигура».
    """
    FIGURE_TYPE = "Геометрическая фигура"

    @abstractmethod
    def square(self):
        pass
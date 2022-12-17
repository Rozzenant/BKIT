from lab_python_oop.box import *
from lab_python_oop.rectangle import *
from lab_python_oop.circle import *
import numpy as np

def main():
    r = Rectangle("синего", 2, 2)
    c = Circle("зеленого", 2)
    s = Box("красного", 2)
    print(r)
    print(c)
    print(s)

    mas = np.array([[1,5,6,5],
                    [3,9,-2,0],
                    [9,4,7,1],
                    [1,0,9,4]])

    print(f"\n{np.linalg.det(mas)}")
    print(mas.dot(mas))

if __name__ == '__main__':
    main()

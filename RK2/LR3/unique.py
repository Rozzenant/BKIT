from gen_random import gen_random
import json

class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self.set = set()
        self.items = items
        self.ignore_case = ignore_case
        self.kwargs = kwargs

    def __next__(self):
        it = iter(self.items)
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise
            else:
                if self.ignore_case == True and isinstance(current, str):
                    a = current[:]
                    if a.lower() not in self.set:
                        self.set.add(a.lower())
                        return current
                elif current not in self.set:
                    self.set.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data1 = ["a", "A", "b", "B", "a", "A", "b", "B"]
    data3 = gen_random(10, 4, 6)
    print(*Unique(data))
    print(*Unique(data1))
    print(*Unique(data1, True))
    print(*Unique(data3))
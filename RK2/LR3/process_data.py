import json
from pprint import pprint
from print_result import print_result
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from unique import Unique


path = 'data_light.json'
with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list(Unique(list(field(arg, "job-name")), True)), key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python', arg))


@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    return [f'{job}, зарплата {salary} руб.' for job, salary in zip(arg, salary)]


if __name__ == '__main__':
    with cm_timer_1():
        pprint(f4(f3(f2(f1(data)))))
        # print(*f4(data))
        pass
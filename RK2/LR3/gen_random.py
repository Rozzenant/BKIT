from random import randint as rand
def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield rand(begin, end)

if __name__ == "__main__":
    print(*gen_random(5, 1, 30))
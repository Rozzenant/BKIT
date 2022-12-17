goods = [
    {'title': 'Ковер',
     'price': 2000,
     'color': 'green'},
    {'title': 'Диван для отдыха',
     'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            yield i.get(args[0])
    else:
        for i in items:
            d = {}
            for a in args:
                if i.get(a) is not None:
                    d[a] = i.get(a)
            yield d


if __name__ == "__main__":
    n1 = field(goods, 'title')
    for i in n1:
        print(i, end=', ')
    print()
    n2 = field(goods, 'title', 'price')
    for i in n2:
        print(i, end=', ')
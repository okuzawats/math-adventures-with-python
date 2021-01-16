def g(x):
    return 6 * x ** 3 + 31 * x ** 2 + 3 * x - 10


def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print('x =', x)
        x += 1


plug()

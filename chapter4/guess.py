def f(x):
    return 6 * pow(x, 3) + 31 * pow(x, 2) + 3 * pow(x, 1) - 10


def pow(x, n):
    return x ** n


def average(a, b):
    return (a + b) / 2.0


def guess():
    lower = -1
    upper = 0
    for i in range(20):
        midpt = average(lower, upper)
        mid = f(midpt)
        if mid == 0:
            return midpt
        elif mid < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt


x = guess()
print(x, f(x))

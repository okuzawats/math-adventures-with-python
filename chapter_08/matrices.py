a = [[1, 2, -3, -1]]
b = [
    [4, -1],
    [-2, 3],
    [6, -3],
    [1, 0],
]


def addMatrices(a, b):
    c = [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]]
    ]
    return c


def multMatrics(a, b):
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k] * b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


c = multMatrics(a, b)
print(c)

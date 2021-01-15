divisor = 2
row = [1, 2, 3, 4, 5]
for i, term in enumerate(row):
    row[i] = term / divisor
print(row)


def gauss(a):
    m = len(a)
    n = len(a[0])
    for j, row in enumerate(a):
        if row[j] != 0:
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor
        for i in range(m):
            if i != j:
                addinv = -1 * a[i][j]
                for ind in range(n):
                    a[i][ind] += addinv * a[j][ind]
    return a


b = [
    [2, 1, -1, 8],
    [-3, -1, 2, -1],
    [-2, 1, 2, -3],
]
print(gauss(b))

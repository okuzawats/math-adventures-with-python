def factors(num):
    """numの約数リストを返す"""
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list


def gcd(a, b):
    return max(set(factors(a)) & set(factors(b)))


print(factors(120))
print(gcd(150, 138))

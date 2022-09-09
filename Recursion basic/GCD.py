from operator import mod


def gcd(n1, n2):
    assert n1 == int(n1) and int(n2) == n2, "number should be integer"
    n1, n2 = abs(n1), abs(n2)
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


print(gcd(56, 98))


# 12 % 8 = 4
# 8 % 4 = 0
# hence gcd is 4

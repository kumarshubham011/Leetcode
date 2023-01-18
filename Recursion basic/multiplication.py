def mul(n1, n2):
    if n1 == 1:
        return n2
    return n2 + mul(n1 - 1, n2)


print(mul(5, 5))

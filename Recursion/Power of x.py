def pow(x, n):
    assert n >= 0 and int(n) == n, "exponnent is invalid"
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)


print(pow(3, 1.4))


# PROGRAM FOR FACTORIAL
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

def zeros(n):
    if n == 0:
        return 0
    iszero = 1 if n % 10 == 0 else 0
    return iszero + zeros(n//10)


print(zeros(10002000))

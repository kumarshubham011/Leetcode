def dsum(num):
    assert num >= 0 and int(num) == num, "number should be positive"
    if num == 0:
        return 0
    else:
        return num % 10 + dsum(num // 10)


print(dsum(999))

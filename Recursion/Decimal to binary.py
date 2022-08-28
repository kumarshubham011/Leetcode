def dtb(n):
    assert int(n) == n, "integer digit not given"
    if n // 2 == 0:  # n == 0
        return n % 2  # return 0
    else:
        return n % 2 + 10 * dtb(n // 2)


print(dtb(15))

def gsum(n):
    if n == 0:
        return 1
    return 1/2**n + gsum(n-1)


print(gsum(4))

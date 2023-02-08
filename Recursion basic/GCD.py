# from operator import mod


# def gcd(n1, n2):
#     assert n1 == int(n1) and int(n2) == n2, "number should be integer"
#     n1, n2 = abs(n1), abs(n2)
#     if n2 == 0:
#         return n1
#     else:
#         return gcd(n2, n1 % n2)


# print(gcd(56, 98))


# 12 % 8 = 4
# 8 % 4 = 0
# hence gcd is 4
n = int(input())
t = int(input())
arr = [0]*n
arr = list(map(int, input().split(" ")))

n, t = 7, 2
r = [5, 3, 3, 3, 5, 6, 2]

days = []


def rain(arr, t, n):
    for i in range(t, n - t):

        ideal = True
        for j in range(i - 1, i - t - 1, - 1):
            if arr[j] < arr[j + 1]:
                ideal = False
                break

        if ideal:
            for j in range(i + 1, i + t + 1):
                if arr[j] < arr[j - 1]:
                    ideal = False
                    break

        if ideal:
            days.append(i + 1)
    return days


print(rain(arr, t, n))

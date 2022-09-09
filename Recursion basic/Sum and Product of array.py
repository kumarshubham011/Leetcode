def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3]))  # 6
print(productOfArray([1, 2, 3, 10]))  # 60


def SumOfArray(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + SumOfArray(arr[1:])


print(SumOfArray([1, 2, 3, 10]))
print(SumOfArray([1, 2, 3, 10, 34, 6]))

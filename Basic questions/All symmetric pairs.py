# code to fins all symmetric pairs
def pairs(arr):
    pair = {}
    n = len(arr)
    res = []

    for n in arr:
        curr = n
        rev = curr[::-1]

        if rev in pair:
            res.append(curr)

        else:
            pair[curr] = True
    return res


print(pairs([(1, 3), (3, 1), (2, 2), (2, 2)]))

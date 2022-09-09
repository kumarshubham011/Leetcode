# def flatten(arr):
#     resultArr = []
#     for custItem in arr:
#         if type(custItem) is list:
#             resultArr.extend(flatten(custItem))
#         else:
#             resultArr.append(custItem)
#     return resultArr


# print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
# print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
# print(flatten([[1], [2], [3]])) # [1, 2, 3]
# print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]


def flat(a):
    res = []
    for ele in a:
        if type(ele) == list:
            res.extend(flat(ele))
        else:
            res.append(ele)
    return res


print(flat([1, 2, 3, [4, 5]]))  # [1, 2, 3, 4, 5]
print(flat([1, [2, [3, 4], [[5]]]]))  # [1, 2, 3, 4, 5]
print(flat([[1], [2], [3]]))  # [1, 2, 3]
print(flat([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # [1, 2, 3]

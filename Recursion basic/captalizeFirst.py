#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# capitalizeFirst Solution

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'taco', 'banana']))  # ['Car','Taco','Banana']


def capital(lst):
    res = []
    if len(lst) == 0:
        return res
    else:
        res.append(lst[0].capitalize())
        return res + capital(lst[1:])


print(capital(['car', 'taco', 'banana']))  # ['Car','Taco','Banana']

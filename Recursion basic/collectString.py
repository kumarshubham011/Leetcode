#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# collectStrings Solution

def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr


obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))  # ['foo', 'bar', 'baz'])


def collectstring(obj):
    res = []
    for key, value in obj.items():
        if type(value) == str:
            res.append(value)
        if type(value) == dict:
            res += collectstring(value)
    return res


print(collectstring(obj))

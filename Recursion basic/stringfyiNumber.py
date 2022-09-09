def stringnum(obj):
    new_obj = obj
    for key, value in new_obj.items():
        if type(value) == dict:
            new_obj[key] = stringnum(value)
        if type(value) is int:
            new_obj[key] = str(new_obj[key])
    return new_obj


obj1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringnum(obj1))
# {'num': '1', 'test': [], 'data': {'val': '4','info': {'isRight': True, 'random': '66'}}}

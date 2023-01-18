def sm(i):
    if i == 0:
        return 0
    return i % 10 + sm(i//10)


print(sm(123455))

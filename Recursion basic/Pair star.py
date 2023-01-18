def pairstar(s):
    if len(s) == 0 or len(s) == 1:
        return s

    if s[0] == s[1]:
        smalloutput = pairstar(s[1:])
        return s[0] + '*' + smalloutput
    else:
        smalloutput = pairstar(s[1:])
        return s[0] + smalloutput


print(pairstar('aaaa'))
print(pairstar('hello'))

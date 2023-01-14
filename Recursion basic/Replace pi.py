def replacepi(s):
    if len(s) == (0 or 1):
        return s

    if s[0] == 'p' and s[1] == 'i':
        smalloutput = replacepi(s[2:])
        # 2 characters will be replaced with pi
        return '3.14' + smalloutput
    else:
        smalloutput = replacepi(s[1:])
        return s[0] + smalloutput


print(replacepi('pipipid'))

def removed(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] != s[1]:
        smalloutput = removed(s[1:])
        return s[0] + smalloutput
    else:
        return removed(s[1:])


print(removed("aabccd"))
print(removed('aaaaabbbbb'))

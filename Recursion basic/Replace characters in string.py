def replacechar(s, a, b):
    if len(s) == 0:
        return s
    # repeatedly call the function on smaller sublist
    smalloutput = replacechar(s[1:], a, b)

    # if first word of string is a then replace it with b and return first replaced substring
    # with the smalloutput
    if s[0] == a:
        return b + smalloutput
    else:
        return s[0] + smalloutput


print(replacechar('abccccd', 'c', 'x'))

# a[bccccd]       abxxxxd
# b[ccccd]        bxxxxd
# c[cccd]         xxxxd
# c[ccd]          xxxd
# c[cd]           xxd
# c[d]            xd
# d               d
# 0

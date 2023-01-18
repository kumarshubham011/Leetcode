def sti(s):
    l = len(s)
    if l == 0:
        return 0
    smalloutput = sti(s[: l-1])
    last_digit = ord(s[l-1]) - ord('0')

    return smalloutput*10 + last_digit


print(sti('000012304'))

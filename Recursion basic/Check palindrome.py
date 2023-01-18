def palin(s, l, r):
    if l <= r:
        if s[l] == s[r]:
            return palin(s, l+1, r-1)
        else:
            return False
    else:
        return True


print(palin('racecar', 0, len('raceca')-1))

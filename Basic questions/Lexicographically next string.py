# Input : geeks
# Output : geekt
# The last character 's' is changed to 't'.

# Input : raavz
# Output : raawz
# Since we can't increase last character,
# we increment previous character.

# Input :  zzz
# Output : zzza
def nextWord(s):

    # If string is empty.
    if (s == " "):
        return "a"

    # Find first character from right
    # which is not z.
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1

    # If all characters are 'z', append
    # an 'a' at the end.
    if (i == -1):
        s = s + 'a'

    # If there are some non-z characters
    else:
        s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

    return s

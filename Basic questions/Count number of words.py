# Given a string consisting of spaces,\t,\n and lower case  alphabets.Your task is to count the number of words where spaces,\t and \n work as separators.
def countWords(s):

    res = 0
    word_started = False
    for i in range(len(s)):
        if s[i] not in [' ', '\n', '\t']:
            if not word_started:
                word_started = True
                res += 1
        else:
            word_started = False
    return res


print(countWords("a\nhjpfo"))

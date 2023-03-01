# Every substring of identical letters is replaced by a single instance of that letter followed by the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it.

class Solution:

    def encryptString(self, s):
        res = ''
        c = 0
        for i in range(len(s)):
            c += 1
            if (i+1) < len(s) and s[i] == s[i+1]:
                continue
            res += s[i]
            res += str(c)
            c = 0
        return res[::-1]

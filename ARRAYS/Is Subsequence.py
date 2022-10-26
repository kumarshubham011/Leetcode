class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                # match is found increment i and j to find for next ele
                i += 1
                j += 1
            else:
                j += 1
        # if i reaches the end of s then we found all matches else not
        return True if i == len(s) else False

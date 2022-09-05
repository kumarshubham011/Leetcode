# METHOD 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for l in s:
            h1[l] = 1 + h1.get(l, 0)
        for l in t:
            h2[l] = 1 + h2.get(l, 0)
        return h1 == h2


# METHOD 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

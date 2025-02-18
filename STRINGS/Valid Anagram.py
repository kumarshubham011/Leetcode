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


#  METHOD 3 - Handles unicode characters 
# The ord() function is the inverse of the chr() function, which converts an integer Unicode code point back into its corresponding character. 
# The ord() function returns the Unicode code point for a one-character string.

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    
    for char in s:
        code_point = ord(char)
        if code_point in count:
            count[code_point] += 1
        else:
            count[code_point] = 1
    
    for char in t:
        code_point = ord(char)
        if code_point in count:
            count[code_point] -= 1
        else:
            return False
    
    for value in count.values():
        if value != 0:
            return False
    
    return True
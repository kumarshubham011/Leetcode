# METHOD 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        while s[j] == " ":
            j -= 1

        count = 0
        while s[j] != " " and j >= 0:
            count += 1
            j -= 1
        return count


# METHOD 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        return len(s[-1])

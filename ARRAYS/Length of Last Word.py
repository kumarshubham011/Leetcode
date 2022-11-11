# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

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

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                # skip left or a right character and check if the new string is palindrome or not in either of the cases
                skipl, skipr = s[left + 1: right + 1], s[left: right]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
            left, right = left+1, right - 1
        return True

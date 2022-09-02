from ast import List

# USING RECURSION


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        def reverse(left, right, string):
            if left <= right:
                s[left], s[right] = s[right], s[left]
                reverse(left + 1, right - 1, s)
        reverse(left, right, s)

# USING TWO POINTERS
    def reverseString(self, s: List[str]) -> None:
        # we will use two pointers and swap the values while left<right
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

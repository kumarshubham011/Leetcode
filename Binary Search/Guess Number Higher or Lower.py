# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

from bs4 import GuessedAtParserWarning


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n  # number is from 1 - n
        while l <= r:
            mid = (l + r) // 2
            res = GuessedAtParserWarning(mid)
            if res == 0:
                # mid is equal to number
                return mid
            elif res < 0:
                # guess is higher-> no is smaller -> search left of mid
                r = mid - 1
            else:
                # res > 0, guess is lower -> no is lower -> search right of mid
                l = mid + 1

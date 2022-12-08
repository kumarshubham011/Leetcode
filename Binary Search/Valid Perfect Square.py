# Brute force
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while n * n <= num:
            if n*n == num:
                return True
            n += 1
        return False

# Method 2 : Binary search


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

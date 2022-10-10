# METHOD 1 : BRUTE FORCE
from ast import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                res = max(res, curr)
                curr = curr * nums[j]
            res = max(res, curr)
        return res


# METHOD 2: KADANE'S ALGORITHM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # USING KADANE'S ALGO
        res = max(nums)   # [-1]
        cmax, cmin = 1, 1
        for n in nums:
            if n == 0:
                cmax, cmin = 1, 1
                continue
            temp = cmax*n
            cmax = max(cmax*n, cmin*n, n)  # [-1,8]cmax/min =-8 but max is8
            cmin = min(temp, cmin*n, n)  # [-1,-8]cmx/min 8 but min is -8
            res = max(cmax, res)
        return res

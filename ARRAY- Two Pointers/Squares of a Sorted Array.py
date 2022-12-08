# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# BRUTE FORCE
from ast import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = []
        for n in nums:
            sq.append(n*n)
        sq.sort()
        return sq


# METHOD 2: USING 2 POINTERS
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        write = len(nums) - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[write] = nums[l] * nums[l]
                l += 1
            else:
                # right is greater and we will add its squared valye at write position
                res[write] = nums[r] * nums[r]
                r -= 1
            write -= 1
        return res

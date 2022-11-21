# Input: nums = [9,4,1,7], k = 2
# Output: 2
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
from ast import List
import math

# SLIDING WINDOW


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mn = math.inf
        nums.sort()
        k = len(nums) - k
        print(nums)
        return nums[-1] - nums[k]

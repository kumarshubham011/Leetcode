# BRUTE FORCE
from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        for i in range(len(nums)):
            currsum = 0
            for j in range(i, len(nums)):
                currsum += nums[j]
                maxsum = max(maxsum, currsum)
        return maxsum


# KADANE'S ALGORITHM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # variable to store maximum sum
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            # if adding an element makes current sum less than 0 then make current sum = 0 and skip that element
            if cur_sum < 0:
                cur_sum = 0
            # otherwise add the element to the current sum and update the maximum sum with larger of two values
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        return max_sum

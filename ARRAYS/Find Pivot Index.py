# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
from ast import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == s-nums[i]-left_sum:
                return i
            left_sum += nums[i]
        return -1

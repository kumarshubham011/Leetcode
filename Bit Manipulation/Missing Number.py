# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from ast import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if both number is 1 or zero xor is 0 otherwise 1
        # xor of any number with 0 is number itself
        # xor of same number with itself is zero
        # we will take a for loop and xor every element in the range n
        # then we will take another for loop and xor the above result with every element in nums, thus repeated number will become zero and missing number will yield itself
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i      # 0^1^2^3

        for n in nums:
            res = res ^ n      # (0^1^2^3) ^ (0^1^3) = 2

        return res

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# METHOD 1- BRUTE FORCE
from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[i+1:]:
                return nums[i]


# METHOD 2 - HASHMAP
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = {}
        for n in nums:
            hashset[n] = 1 + hashset.get(n, 0)
        for key, value in hashset.items():
            if hashset[key] < 2:
                return key


# METHOD 3 - BIT MANIPULATION
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

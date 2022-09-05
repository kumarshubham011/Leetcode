# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# METHOD 1
from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        s = set(nums)
        for i in range(1, n+1):
            if i not in s:
                res.append(i)
        return res


# METHOD 2 - USING NEGATION
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            # abs is taken because some elements may already be negated.
            # and negative indexing is to be avoided here
            nums[abs(n)-1] = -abs(nums[abs(n)-1])

        for i in range(len(nums)):
            # if number is positive at index i, it means the number at that index has not been negated and element i+1 is not present in nums
            if nums[i] > 0:
                res.append(i+1)
        return res

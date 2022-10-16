# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# METHOD 1:
from ast import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # if length of array is 0 then it is already sorted
        if len(nums) == 0:
            return True

        # we found out the pivot element, the index from where the array is rotated
        piv = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                piv = i
                break
        # if pivot index is 0, means array is already sorted
        if piv == 0:
            return True
        # if num at starting is less than last num then condition is not met--> False
        if piv != 0 and nums[0] >= nums[-1]:
            for j in range(0, piv):
                if nums[j] < nums[j-1]:
                    return False
            for k in range(piv+1, len(nums)):
                if nums[k] < nums[k-1]:
                    return False
            return True


# METHOD 2:
class Solution:
    def check(self, nums: List[int]) -> bool:
        # compare count of nums[i] < nums[i-1]
        # there are three possible cases
        # CASE 1: array is already sorted i.e count == 0 -->> return true
        # CASE 2: count is 1 -->> return true
        # CASE 3 : count is greater than 1 -->> return false
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
        # edge case
        if nums[0] < nums[-1]:
            count += 1
        return True if count <= 1 else False

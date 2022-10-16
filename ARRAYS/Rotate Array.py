# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]


# METHOD 1: O(N) SPACE COMPLEXITY
from ast import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[(i+k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = res[i]
        return nums


# METHOD 2: O(N) SPACE, TIME COMPLEXITY
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # if the list if required to rotate len(nums) number of times then there is no rotations required
        k = k % len(nums)

        l, r = 0, len(nums)-1
        # reversing the array
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # reversing 1st k elements
        l, r = 0, k-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # reversing last n-k elements
        l, r = k, len(nums)-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

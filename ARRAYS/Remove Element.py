# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we will use two pointers approach
        # if l == val we swap l with r and decrement r so that comaprison with nexr element can be made
        # if l is not equal to val then we increment l
        # we repeat until l surpasses r beacuse after that all values will be equal to val
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return l

from typing import List


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

# default template for binary search
from ast import List

# SOLUTION 1


def binary_search(low, hi, condition):
    # condition is function passed as parameter
    while low <= hi:
        mid = (low+hi)//2
        res = condition(mid)
        if res == 'found':
            return mid
        elif res == 'left':
            hi = mid-1
        elif res == 'right':
            low = mid+1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_position(nums, target):
            def condition(mid):
                if nums[mid] == target:
                    if nums[mid-1] == target and mid > 0:
                        return 'left'
                    return 'found'
                elif nums[mid] > target:
                    return 'left'
                elif nums[mid] < target:
                    return 'right'
            return binary_search(0, len(nums)-1, condition)

        def last_position(nums, target):
            def condition(mid):
                if nums[mid] == target:
                    if mid < len(nums)-1 and nums[mid+1] == target:
                        return 'right'
                    return 'found'
                elif nums[mid] > target:
                    return 'left'
                elif nums[mid] < target:
                    return 'right'
            return binary_search(0, len(nums)-1, condition)
        return first_position(nums, target), last_position(nums, target)


# SOLUTION 2
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binary_search(nums, target, True)
        r = self.binary_search(nums, target, False)
        return [l, r]

    def binary_search(self, nums, target, leftBias):
        # if leftBias is true then we will search fot 1st occurrence of the number in left side of mid if that number exist in left side.
        left, right = 0, len(nums)-1
        i = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid+1
            else:
                i = mid
                # we will check if target's occurence to the left and right of mid depending upon the condition leftBias
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i

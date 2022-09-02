from ast import List

# ITERATIVE APPROACH


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid - 1
        return -1

# RECURSIVE APPROACH
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        def bin_search(left, right, nums):
            if left > right:
                return -1

            else:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return bin_search(mid + 1, right, nums)
                elif nums[mid] > target:
                    return bin_search(left, mid - 1, nums)
        return bin_search(left, right, nums)

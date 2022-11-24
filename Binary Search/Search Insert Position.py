from ast import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left
        # Note that it would exit the while loop ONLY when target is not in nums. When this happens, the if and else statement in the last loop will also adjust left so we simply return left at the end.

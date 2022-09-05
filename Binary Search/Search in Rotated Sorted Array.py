# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# SOLUTION 1
from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.count_rotations_binary(nums)
        print(pivot)
        lo, hi = 0, len(nums)-1
        # if target is greater than 1st element then it lies in left sorted array
        # else it lies in right sorted array
        # print("hi:",hi)
        if pivot != 0:
            if target >= nums[0]:
                hi = pivot-1

            else:
                lo = pivot
            #print("lo:", lo, ", hi:", hi)

        # Now performing normal binary searh to find out target psoition
        while lo <= hi:
            mid = lo+(hi-lo)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid+1
            else:
                hi = mid-1
        return -1

    def count_rotations_binary(self, nums):
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2
            mid_number = nums[mid]

            #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

            if mid > 0 and nums[mid] < nums[mid-1]:
                # The middle position is the answer
                return mid

            elif nums[mid] < nums[len(nums)-1]:
                # Answer lies in the left half
                hi = mid - 1

            else:
                # Answer lies in the right half
                lo = mid + 1

        return 0


# METHOD 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted section
            elif nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right sorted section
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

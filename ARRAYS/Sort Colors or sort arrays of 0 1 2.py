# BRUTE FORCE:
# Directly sort the array

# METHOD 2: Keep count of zeros , ones , and twos.
from ast import List


class Solution:
    def sort012(self, arr, n):
        zeros = 0
        ones = 0
        twos = 0
        for n in arr:
            if n == 0:
                zeros += 1
            if n == 1:
                ones += 1
            if n == 2:
                twos += 1
        i = 0
        while i < zeros:
            arr[i] = 0
            i += 1
        while i < zeros + ones:
            arr[i] = 1
            i += 1
        while i < zeros + ones + twos:
            arr[i] = 2
            i += 1
        return arr


# METHOD 3: THREE POINTERS :-> O(N)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # we will use three pointers lo,mid,hi. We will assign lo,mid to zeroth index and hi to last index.

        # The idea is: elements from 0 to lo-1  will contain zeros, elements from lo to mid-1 will contain ones, elemetns from hi to end will contain 2

        # we will move the mid pointer and if zero is encountered we will swap lo and mid and increments both of them, if one is encountered we will only move mid, and if 2 is encountered we will swap elements of mid and hi, and decrement hi.

        # MID is not incremented in case when mid == 2 because it may arise in 0 being in middle of array rather than being in left side of lo.
        lo = 0
        mid = 0
        hi = len(nums)-1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
        return nums

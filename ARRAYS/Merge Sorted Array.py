# METHOD 1 : BRUTE FORCE
from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0]*(m+n)
        for i in range(m):
            nums3[i] = nums1[i]
        for j in range(n):
            nums3[j+m] = nums2[j]
        nums3.sort()

        for k in range(m+n):
            nums1[k] = nums3[k]
        return nums1


# METHOD 2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # take a pointer i and use it to compare elements of nums1 with first element of nums2
        # if it is greater than first element of nums2, swap them both and increment the pointer
        # then rearrange the elemets in nums2 to sort them

        for i in range(m):
            if len(nums2) == 0:
                return nums1
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
            print(nums1)
            # making nums2 ordered again
            for j in range(1, n):
                if nums2[j] < nums2[j-1]:
                    nums2[j-1], nums2[j] = nums2[j], nums2[j-1]

        # merging both arrays
        for k in range(n):
            nums1[k+m] = nums2[k]
        return nums1

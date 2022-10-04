from ast import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i, j = len(nums) - 1, len(nums) - 1
        # find the index whose element is lesser than element after that index
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:  # numbers are in descemding order
            nums.reverse()
            return

        k = i - 1  # k is the pivot element after which all elements are greater than it
        # find the index of element which is larger than kth element,  from end
        while nums[j] <= nums[k]:
            j -= 1

        # swap pivot element i.e K and J
        nums[k], nums[j] = nums[j], nums[k]

        # reverse element after the pivot element
        l, r = k + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

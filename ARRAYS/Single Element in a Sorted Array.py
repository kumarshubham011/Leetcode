from ast import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # METHOD 3 - BINARY SEARCH
        l, r = 0, len(nums)
        while l <= r:
            m = l + ((r-l) // 2)

            # if the midpoint is the single non-duplicate element, return it
            if ((m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m] != nums[m+1])):
                return nums[m]

            # determine which side of the midpoint contains an even number of elements
            leftSize = m-1 if nums[m-1] == nums[m] else m

            # if the left side contains an even number of elements, the single element must be on the right
            if leftSize % 2 == 0:
                l = m + 1
            # otherwise, the single element must be on the left
            else:
                r = m - 1

        # METHOD 1 - HASHMAP
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        print(hashmap)
        for key, value in hashmap.items():
            if value == 1:
                return key

        # METHOD 2 - BIT MANIPULATION
        res = 0
        for n in nums:
            res = res ^ n
        return res

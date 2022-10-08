from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # we have to check if the element next to i is same as i, if yes for loop will icrement i without performing below operations
            if i > 0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]
            l, r = i + 1, len(nums)-1

            while l < r:
                if nums[l] + nums[r] + n1 == 0:
                    res.append([n1, nums[l], nums[r]])
                    # updating the left pointer so that if a duplicate value is encountered it skips it.
                    # right pointer will auto update itself due to next two elif conditions.
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif nums[l] + nums[r] + n1 > 0:
                    r -= 1
                elif nums[l] + nums[r] + n1 < 0:
                    l += 1
        return res

from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # we will iterate over the nums and if we encounter 0 we make the count zero otherwise we increment the count
        # to find the maxm consecutive ones, we compare the count and maxi and whichever is larger we update the value of maxi with it
        count = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxi = max(count, maxi)
            elif nums[i] == 0:
                count = 0
        return maxi

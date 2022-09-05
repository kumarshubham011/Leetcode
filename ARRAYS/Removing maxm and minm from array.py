from ast import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # first find minimum and maximum element in array
        minm, maxm = min(nums), max(nums)

        # find the index of minimum and maximum
        min_i, max_i = nums.index(minm), nums.index(maxm)

        # now, there will be 3 scenarios,
        # 1st when deletions have to be made from rear only
        d1 = max(min_i, max_i)+1

        # 2nd when deletions have to be made from front only
        d2 = len(nums) - min(min_i, max_i)

        # when deletions have to be made from both front and rear
        left_d = min(min_i, max_i)+1
        right_d = len(nums)-max(min_i, max_i)
        d3 = left_d+right_d

        return min(d1, d2, d3)

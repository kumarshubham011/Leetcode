# METHOD 1 : BRUTE FORCE
from ast import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sm = nums[i]
            if sm == k:
                res += 1

            for j in range(i+1, len(nums)):
                sm += nums[j]
                if sm == k:
                    res += 1
        return res


# METHOD 2 : USING HASHMAP :-> O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix_sum = {0: 1}
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            # if we can remove the difference from the current sum then we can get the required sum

            res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)
        return res

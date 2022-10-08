# BRUTE FORCE USING HASHMAP
from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force using hashmap
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        res = []
        for key, value in hashmap.items():
            if value > len(nums)/3:
                res.append(key)
        return res


# METHOD 2 : USING BOYER MOORE VOTING ALGORITHM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using Boyer Moore Voting Algorithm
        nums1, nums2 = 0, -1
        c1, c2 = 0, 0
        for n in nums:
            if n == nums1:
                c1 += 1
            elif n == nums2:
                c2 += 1

            elif c1 == 0:
                nums1 = n
                c1 = 1

            elif c2 == 0:
                nums2 = n
                c2 = 1

            else:
                c1 -= 1
                c2 -= 1

        res = [n for n in (nums1, nums2) if nums.count(n) > len(nums)/3]
        return res

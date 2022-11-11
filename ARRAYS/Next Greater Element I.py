# O(N*M) SOLUTION
from ast import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # storing index of each elements of nums1 in hashmap
        nums1idx = {}
        for i in range(len(nums1)):
            nums1idx[nums1[i]] = i
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1idx:
                continue
            # second for loop for iterating to find next greater element
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    # find index of nums2[i] from hashmap
                    idx = nums1idx[nums2[i]]
                    # store next greater element i.e nums2[j] at idx
                    res[idx] = nums2[j]
                    break
        return res

# O(N + M)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(M + N)
        # storing index of each elements of nums1 in hashmap
        nums1idx = {}
        for i in range(len(nums1)):
            nums1idx[nums1[i]] = i
        res = [-1] * len(nums1)
        # using monotonic stack
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                value = stack.pop()
                # find index of the value cause its next greater element is curr
                idx = nums1idx[value]
                res[idx] = curr
            if curr in nums1idx:
                stack.append(curr)

        return res

from ast import List

# METHOD 1 - HASHMAP


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we will use hashmap, if target-num is already in hashmap, we will return the index of number and the value of target-num in hash map.
        # else we will add the num in hasmap and move on to next element in nums.
        prevEle = {}
        for i in range(len(nums)):
            if target-nums[i] in prevEle:
                # found out the index of target-nums[i]
                ind = nums.index(target-nums[i])
                return i, ind
            else:
                prevEle[nums[i]] = i


# METHOD 2- O(N^2)


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                ind = nums.index(target-nums[i], i+1)
                return i, ind


# METHOD 3- BRUTE FORCE


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i, j

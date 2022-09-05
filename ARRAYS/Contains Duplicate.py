# Input: nums = [1,2,3,1]
# Output: true

# METHOD 1
from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hashtable
        hashset = {}
        # iterate through nums and add it to the hashset as key with total number of occurences as its value
        for n in nums:
            hashset[n] = hashset.get(n, 0) + 1

        # iterate through hashset and if a key has value greater than 1 then return true
        for i in hashset:
            if hashset[i] >= 2:
                return True
        return False


# METHOD 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rep_rec = set()
        for i in nums:
            if i in rep_rec:
                return True
            else:
                rep_rec.add(i)
        return False


# METHOD 3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        var = set(nums)
        return len(var) != len(nums)


# METHOD 4 - SORTING
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

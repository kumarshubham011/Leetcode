# BRUTE FORCE
from ast import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        longest_streak = 0
        for n in nums:
            current_num = n
            current_streak = 1

            while current_num + 1 in nums:
                current_streak += 1
                current_num += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak


# METHOD 2: -> SORTING
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # SORTING
        if len(nums) == 0:
            return 0
        longest_streak = 1
        count = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                longest_streak = max(longest_streak, count)
            else:
                count = 1

        return longest_streak


# METHOD2 :-> HASHSET
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxi = 0

        for n in hashset:
            # check if n is starting of the sequence
            if n-1 not in hashset:
                count = 0
                while count + n in hashset:
                    # count+n is basically n itself in the begining
                    count += 1
                maxi = max(count, maxi)
        return maxi

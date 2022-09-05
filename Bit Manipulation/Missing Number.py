# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from ast import List

# METHOD 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if both number is 1 or zero xor is 0 otherwise 1
        # xor of any number with 0 is number itself
        # xor of same number with itself is zero
        # we will take a for loop and xor every element in the range n
        # then we will take another for loop and xor the above result with every element in nums, thus repeated number will become zero and missing number will yield itself
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i      # 0^1^2^3

        for n in nums:
            res = res ^ n      # (0^1^2^3) ^ (0^1^3) = 2

        return res

# METHOD 2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # there will be total n+1 numbers in range 0 to n
        n = len(nums)+1

        # we will calculate the expected sum in range 1-n by using the formulae for sum of an arithmaic progression with symmetric difference one.
        exp_sum = int(n/2*(n-1))

        sum = 0
        for i in nums:
            sum += i
        return exp_sum-sum


# METHOD 3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_nums = [num for num in range(n+1)]
        for n in all_nums:
            if n in nums:
                continue
            return n

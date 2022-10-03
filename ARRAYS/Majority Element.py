# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# METHOD 1 : HASHMAP
from ast import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use a hashtable to store the count of each number
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        # find out which key occurs maxm numbers of time
        # then find out if that value occurs more than n/2 times in array
        max_occur = 0
        res = -math.inf
        for key, value in hashmap.items():
            if value > max_occur:
                max_occur = value
                res = key
        return res


# METHOD 2 :-> Moore’s Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use two variables count and res
        count = 0
        res = 0
        for n in nums:
            # initialize the current traversing element as res if count == 0
            if count == 0:
                res = n

            # increment count if same number is encountered, decrement otherwise
            count += (1 if n == res else -1)
        return res

# Initialize 2 variables:
# Count –  for tracking the count of element
# Element – for which element we are counting

# Traverse through nums array.

# If Count is 0 then initialize the current traversing integer of array as Element
# If the traversing integer of array and Element are same increase Count by 1
# If they are different decrease Count by 1


# The integer present in Element is the result we are expecting

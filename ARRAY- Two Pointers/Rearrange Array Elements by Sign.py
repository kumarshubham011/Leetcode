# BRUTE FORCE
from ast import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        j, k = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[j]
                j += 1
            else:
                nums[i] = neg[k]
                k += 1
        return nums


# TWO POINTERS
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # TWO POINTERS APPROACH
        # p pointer at 0 index , n at 1 :-> if positive number is encountered add it at p index and increment it by 2
        # else add element at negative index and increment it by 2
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for n in nums:
            if n > 0:
                res[pos] = n
                pos += 2
            else:
                res[neg] = n
                neg += 2
        return res

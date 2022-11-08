
# USING TWO POINTERS TECHNIQUE

from typing import Optional
from typing import List


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        # take 2 pointers, one at start and other at end
        # get the sum if sum == target, then pair is found,
        # if sum > target, dec end pointers else inc start pointer
        res = []
        left = right = head
        while right.next:
            right = right.next
        while left != right:
            sm = left.data + right.data
            if sm == target:
                res.append([left.data, right.data])
            if sm > target:
                right = right.prev
            else:
                left = left.next
        return res

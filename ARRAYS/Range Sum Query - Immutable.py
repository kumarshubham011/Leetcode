# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# USING PREFIX SUM
from ast import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sm = 0
        for n in nums:
            sm += n
            self.prefix.append(sm)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        # if left == 0  then left is start and sum before it is 0

        return rightSum - leftSum


# ex =     [-2,0,3,-5,2,-1]
# prefix = [-2,-2,1,-4,-2,-3]
# left = 2 right = 5
# leftsum at 2 = 1  rightsum at 5 = -3
# res = leftsum at 2-1  - rightsum
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

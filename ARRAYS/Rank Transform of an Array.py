# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
# METHOD 1 - BRUTE FORCE
from ast import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # set operation because arr may contain duplicate items
        copy = sorted(set(arr))
        res = []
        for n in arr:
            # 1 is added because rank satrts from 1 not 0
            res.append(copy.index(n) + 1)
        return res


# METHOD 2 : USING HASHMAP

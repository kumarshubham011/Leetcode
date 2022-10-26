# MY SOLUTION
from ast import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        cmax = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            if arr[i] >= cmax:
                res.insert(0, arr[i])
                cmax = max(cmax, arr[i])
                continue
            res.insert(0, cmax)
        return res


# OPTIMAL SOLUTION
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # at first rightmax = -1
        # iterate in reverse order
        # maintain cmax = max(arr[i], rightmax)
        rightmax = -1
        for i in range(len(arr)-1, -1, -1):
            cmax = max(rightmax, arr[i])
            arr[i] = rightmax
            rightmax = cmax
        return arr

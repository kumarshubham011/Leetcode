# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
from ast import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        from collections import Counter
        cnt = Counter(arr1)

        # first add the elements acc to order of second array
        for n in arr2:
            res = res + [n] * cnt[n]
            cnt[n] = 0
            # count of n is made zero because all of n is already added in res

        out = []
        # make a list to store the elements of dic whose value is not zero
        for key, value in cnt.items():
            if value > 0:
                out = out + [key] * value
        out.sort()

        return res + out

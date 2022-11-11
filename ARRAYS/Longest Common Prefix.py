# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from ast import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we will use a for loop to iterate over the element of first string and a secong for loop for iterating over the elements of each strings

        # if the elements match we will append it to the result else we will return the result
        res = ''
        for i in range(len(strs[0])):
            # we will compare the first element of each string
            curr = strs[0][i]
            for s in strs:
                if i == len(s) or curr != s[i]:
                    return res
            # else s[i] is common prefix
            res += s[i]
        return res

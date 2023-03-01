# User function Template for python3

class Solution:

    # Function to calculate sum of all numbers present in a string.
    def findSum(self, s):
        res = 0
        csum = 0
        for c in s:
            if c.isdigit():
                csum = csum*10 + int(c)
            else:
                res += csum
                csum = 0
        res += csum
        # adds remaining digit if left in csum
        return res

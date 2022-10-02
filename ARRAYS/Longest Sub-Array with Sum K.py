# Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.


# Method 1 : BRUTE FORCE
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        max_length = 0
        for i in range(n):
            sm = 0
            for j in range(n):
                sm += arr[j]
                if sm == k:
                    max_length = max(max_length, j-i+1)
        return max_length


# METHOD 2 : PREFIX SUM

class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        length = 0
        sm = 0
        # handle the case when a sublist with sum `S` starts from index 0
        prefixsum = {0: -1}
        for i in range(n):
            sm += arr[i]
            if sm not in prefixsum:
                prefixsum[sm] = i
            if (sm - k) in prefixsum:
                length = max(length, i - prefixsum[sm-k])
        return length

        # METHOD 3

        # # dictionary mydict implemented
        # # as hash map
        # mydict = dict()

        # # Initialize sum and maxLen with 0
        # sum = 0
        # maxLen = 0

        # # traverse the given array
        # for i in range(n):

        #     # accumulate the sum
        #     sum += arr[i]

        #     # when subArray starts from index '0'
        #     if (sum == k):
        #         maxLen = i + 1

        #     # check if 'sum-k' is present in
        #     # mydict or not
        #     elif (sum - k) in mydict:
        #         maxLen = max(maxLen, i - mydict[sum - k])

        #     # if sum is not present in dictionary
        #     # push it in the dictionary with its index
        #     if sum not in mydict:
        #         mydict[sum] = i

        # return maxLen

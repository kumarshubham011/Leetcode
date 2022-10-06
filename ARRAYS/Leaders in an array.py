# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.

# BRUTE FORCE

class Solution:
    def leaders(self, A, N):
        res = []
        for i in range(N):
            curr = A[i]
            flag = True
            for j in range(i+1, N):
                if A[j] > curr:
                    flag = False
                    break

            if flag == True:
                res.append(curr)
        return res

# METHOD 2


class Solution:
    def leaders(self, A, N):
        res = [A[N-1]]

        i = N-2
        curr_max = A[N-1]
        while i >= 0:
            if A[i] >= curr_max:
                res.append(A[i])
                curr_max = A[i]
            i -= 1
        res.reverse()
        return res

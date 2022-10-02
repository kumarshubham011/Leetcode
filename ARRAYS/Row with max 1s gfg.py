# METHOD 1 : BRUTE FORCE
class Solution:

    def rowWithMax1s(self, arr, n, m):
        count = 0
        a = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    count += 1
            a.append(count)
            count = 0
        return a.index(max(a)) if max(a) != 0 else -1


# METHOD 2: BINARY SEARCH :-> O(N*LOG(M))
# class Solution:

# 	def rowWithMax1s(self, arr, n, m):
# 		count_max = 0  # maxm count of 1
# 		row = -1  # row containing maxm count of 1
# 		for i in range(n):
# 		    count_of_1 = self.binary_search(arr, i)  # i is row for searching 1

# 		    if count_of_1 > count_max:
# 		        count_max = count_of_1
# 		        row = i
# 	    return row

#     def binary_search(self,arr, i):
#         left, right = 0, m-1
#         first_ind_1 = m
#         while left <= right:
#             mid = (left+right)//2
#             if arr[i][mid] == 1:
#                 first_ind_1 = mid
#                 right = mid -1
#             else:
#                 left = mid + 1
#         cout = m - first_ind_1
#         return cout

# METHOD 3: O(N+M)
# class Solution:

# 	def rowWithMax1s(self,arr, n, m):
# 		res_row = -1
# 		i,j = 0, m-1 # i tracks row and j tracks column
# 		while i < n and j >= 0:
# 		    if arr[i][j] == 1:
# 		        res_row = i
# 		        j -= 1 # j decremented to see if previous element is one or not
# 		    elif arr[i][j] == 0:
# 		        i += 1
# 	    return res_row

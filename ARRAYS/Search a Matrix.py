class Solution:
    def matSearch(self, mat, N, M, X):
        i, j = 0, M-1
        while i < N and j >= 0:
            # j moves left i.e column get decremented towards left
            # i moves towards bottom i.e row number gets incremented
            if mat[i][j] == X:
                return 1
            elif mat[i][j] < X:
                i += 1
            elif mat[i][j] > X:
                j -= 1
        return 0

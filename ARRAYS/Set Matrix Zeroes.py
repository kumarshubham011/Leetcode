# BRUTE FORCE: USING EXTRA MEMORY
from ast import List


class Solution(object):
    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# METHOD 2: USING O(M+N) MEMORY
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(M+N) SPACE
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])

        # if we encounter a zero while traversing the matrix, mark the respective row and column index as true
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        # mark the elements of matrix zero if respective rows or cols is True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] is True or cols[j] is True:
                    matrix[i][j] = 0


# METHOD 3 : O(1) MEMORY
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1) SPACE
        r, c = len(matrix), len(matrix[0])
        rowzero = False  # to track if we need to make first row 0

        # determining which rows and cols need to be 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    # column to be zeroed is marked
                    matrix[0][j] = 0

                    if i > 0:
                        # row to be zeroed is marked
                        matrix[i][0] = 0
                    else:
                        rowzero = True

        # marking rows and cols zeros (except row 0 and column 0)
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # making 1st col zero if req
        if matrix[0][0] == 0:
            for i in range(r):
                matrix[i][0] = 0

        # making 1st row zero
        if rowzero == True:
            for i in range(c):
                matrix[0][i] = 0

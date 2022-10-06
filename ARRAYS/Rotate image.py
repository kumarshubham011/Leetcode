# METHOD 1 : 4-WAY SWAP

from ast import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save top-left in temp variable
                topleft = matrix[top][left + i]

                # shift bottomleft value to topleft
                matrix[top][left + i] = matrix[bottom - i][left]

                # shift bottomright value to bottomleft
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # shift topright value to bottomright
                matrix[bottom][right - i] = matrix[top + i][right]

                # shift topleft to topright
                matrix[top + i][right] = topleft

                # update value of top bottom  left right

            left += 1
            right -= 1


# METHOD 2: TRANSPOSING AND REVERSING
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse the matrix
        # transpose the matrix
        l, r = 0, len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

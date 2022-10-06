from ast import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        d = 0
        while left <= right and top <= bottom:
            if d == 0:
                # print left to right
                for i in range(left, right + 1):
                    # row remains fixed i.e top
                    res.append(matrix[top][i])
                top += 1

            elif d == 1:
                # print top to bottom
                for i in range(top, bottom + 1):
                    # col remains fixed i.e right
                    res.append(matrix[i][right])
                right -= 1

            elif d == 2:
                # print right to left
                for i in range(right, left - 1, -1):
                    # bottom row remains fixed
                    res.append(matrix[bottom][i])
                bottom -= 1

            elif d == 3:
                # print from bottom to top
                for i in range(bottom, top - 1, -1):
                    # col remains fixed i,e left
                    res.append(matrix[i][left])
                left += 1
            d = (d + 1) % 4
        return res

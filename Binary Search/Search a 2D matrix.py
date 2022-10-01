from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search to find out which row to search for our target value
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            midrow = (top + bot) // 2
            row = matrix[midrow]
            if row[0] > target:
                bot = midrow - 1
            elif row[-1] < target:
                top = midrow + 1
            else:
                # we found our target row, again apply binary search to find out target value
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] > target:
                        right = mid - 1
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        # we found target
                        return True
                return False

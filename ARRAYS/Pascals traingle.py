from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # idea is we will append zeroes at starting and end of each row, then add two consecutive elements and append it to an empty array and then append that array to the final result array.
        res = [[1]]
        # first row contains only one element 1

        for i in range(numRows-1):
            # adding zeroes at starting and end of each row
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                # no of colums will be one more than the length of last row of the triangle
                # we used two pointers to add the two consecutive element
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res

# use elements as index and mark the visited places
class Solution:
    def findTwoElement(self, arr, n):
        res = []
        # for repeating number
        for i in range(n):
            if arr[abs(arr[i]) - 1] > 0:
                # mark the element as visited or already present in array
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            else:
                # if for a certain number the no at the corresponding index is -ve
                # then we have found the repeating number
                res.append(abs(arr[i]))

        # for missing number
        # iterate over the array, if the element at given index is +ve
        # that means index+1 is missing number
        for i in range(n):
            if arr[i] > 0:
                res.append(i+1)
        return res

# ITERATIVE APPROACH
class Solution:
    def insertionSort(self, alist, n):
        # first element is sorted, start outer loop from 1st element
        for i in range(1, n):
            curr = alist[i]
            j = i - 1
            # if i th element is less than j th element, swap them
            # till j >= 0
            # if not simply add i th element to sorted list part
            while j >= 0 and curr < alist[j]:
                alist[j + 1] = alist[j]
                j -= 1
            alist[j + 1] = curr
        return alist


# RECURSIVE APPROACH
class Solution:

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        if n <= 1:
            return

        # sort first n-1 elements
        Solution.insertionSort(self, alist, n-1)
        curr = alist[n-1]
        j = n - 2
        # if i th element is less than j th element, swap them
        # till j >= 0
        # if not simply add i th element to sorted list part
        while j >= 0 and curr < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = curr

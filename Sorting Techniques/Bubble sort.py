# For the Worst case:
# Total number of swaps = Total number of comparison
# Total number of comparison (Worst case) = n(n-1)/2
# Total number of swaps (Worst case) = n(n-1)/2

# METHOD 1: ITERATIVE

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        for i in range(n - 1):
            swapped = False

            for j in range(n - 1 - i):
                # n-1-i beacause after each iteration maxm digit reaches the last
                # and we do not need to recompare digits with it again
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j + 1], arr[j]
                    swapped = True
            if swapped == False:
                break
        return arr


# METHOD 2 : RECURSIVE BUBBLE SORT
class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):

        for j in range(n - 1):
            # n-1-i beacause after each iteration maxm digit reaches the last
            # and we do not need to recompare digits with it again
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
        if n-1 > 1:
            Solution.bubbleSort(self, arr, n-1)
        return arr

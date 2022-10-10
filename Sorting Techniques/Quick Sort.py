class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            piv = self.partition(arr, low, high)
            self.quickSort(arr, low, piv-1)
            self.quickSort(arr, piv+1, high)

    def partition(self, arr, low, high):
        piv_index = low
        piv_ele = arr[piv_index]

        while low < high:
            # find index where ele is greater than pivot element
            while low < len(arr) and arr[low] <= piv_ele:
                low += 1
            # find index where ele is less than pivot element
            while arr[high] > piv_ele:
                high -= 1

            # swap low and high elements
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]

        # now swap end and pivot element index
        arr[high], arr[piv_index] = arr[piv_index], arr[high]
        return high

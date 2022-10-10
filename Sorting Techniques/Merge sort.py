class Solution:
    def merge(self, arr, l, m, r):
        list1 = arr[l:m+1]
        list2 = arr[m+1:r+1]
        l1 = len(list1)
        l2 = len(list2)

        i = j = 0
        k = l

        while i < l1 and j < l2:
            if list1[i] <= list2[j]:
                arr[k] = list1[i]
                i += 1
                k += 1
            else:
                arr[k] = list2[j]
                j += 1
                k += 1

        while i < l1:
            arr[k] = list1[i]
            i += 1
            k += 1

        while j < l2:
            arr[k] = list2[j]
            j += 1
            k += 1
        return arr

    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l+r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)

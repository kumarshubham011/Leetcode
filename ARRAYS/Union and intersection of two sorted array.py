# INTERSECTION OF TWO SORTED ARRAY
class Solution:
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        res = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                # they are equal
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
                i += 1
        return res


# UNION OF TWO SORTED ARRAY
# METHOD 1: BRUTE FORCE

class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        r = a + b
        r = list(set(r))
        r.sort()
        return r


# METHOD 2 : OPTIMISED TWO POINTERS
class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        res = []
        i, j = 0, 0
        while i < n and j < m:
            if a[i] <= b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                # a[i] > b[j]
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1

        # adding remaining elements of a
        while i < n:
            if res[-1] != a[i]:
                res.append(a[i])
            i += 1

        # adding remaining elements of b
        while j < m:
            if res[-1] != b[j]:
                res.append(b[j])
            j += 1
        return res

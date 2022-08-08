from ast import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
            Since we have to solve this problem in constant space complexity so the only way is to use the space of given array and manipulate it.
            Since the elements in the array are in range [1..n], we can consider the elements as idexes also and to be precise (element - 1) as it is a 0-indexed array.
            Since we can't use any extra space so let us mark the elements encountered in the given array only. This can be done by multiplying the element with -1.
            Now for each element, we will treat it as the index and check whether the value present at that index is visited or not. If it is visited then it is a duplicate else we mark that element as visited(multiply by -1).
        """
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] *= -1
            else:
                res.append(n)
        return res


# if the elements are from range 0 to n-1 and result has to be in sorted order then use  following technique:
"""
Approach: The basic idea is to use a HashMap to solve the problem. But there is a catch, the numbers in the array are from 0 to n-1, and the input array has length n. So, the input array can be used as a HashMap. While Traversing the array, if an element ‘a’ is encountered then increase the value of a%n‘th element by n. The frequency can be retrieved by dividing the a % n’th element by n.
"""


class Solution:
    def duplicates(self, arr, n):
        res = []
        for i in range(n):
            index = arr[i] % n
            arr[index] += n
        for i in range(n):
            if arr[i] >= 2*n:
                res.append(i)

        if len(res) == 0:
            return [-1]
        else:
            return res

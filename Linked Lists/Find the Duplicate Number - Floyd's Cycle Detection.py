from ast import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we will use floyd's algorithms
        # this is a link list cycle problem, we will use fast and a slow pointer.
        # move the fast pointer by 2 and slow pointer by 1, they will intersect at a point.
        # take another pointer, point it at 0 then move this and the slow pointer by 1, the point at which both pointers will intersect is duplicate.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow

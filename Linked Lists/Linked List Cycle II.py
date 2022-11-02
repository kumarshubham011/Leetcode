# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Traverse linked list using two pointers.
# Move one pointer(slow_p) by one and another pointer(fast_p) by two.
# If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.

# But our focus is on where the cycle has started. So, for that once they meet [slow == fast] then, we will reset the slow back to head & start moving slow with 1X speed and fast will carry on from where it was previously but with 1X speed


class Solution:
    def detectCycle(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp
        return None

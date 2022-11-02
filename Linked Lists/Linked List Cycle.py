from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        while head:
            if head in hashSet:
                return True
            hashSet.add(head)
            head = head.next
        return False


# METHOD 2 : FAST AND SLOW POINTERS
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we will use fast and slow pointer, move fast pointer by 2 and slow pointer by one
        # if they both intersect then ll contains cycle else no
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

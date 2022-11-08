# METHOD 1: FAST AND SLOW POINTERS
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        # first find the middle of the ll using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # take a temp var and iterate it to one node before the middle node
        temp = head
        while temp and temp.next != slow:
            temp = temp.next
        temp.next = slow.next
        return head

# METHOD 2:


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        # first find the middle of the ll using fast and slow pointers
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head

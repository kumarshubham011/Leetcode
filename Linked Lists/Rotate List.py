# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # calc length of ll
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # move temp to pivot and perform rotation
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        newhead = temp.next  # this will be head of new ll
        temp.next = None
        tail.next = head

        return newhead

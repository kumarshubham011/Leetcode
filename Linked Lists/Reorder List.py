from tkinter.tix import ListNoteBook
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the linked list into two parts, using fast and slow pointers technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the linked list
        current = slow.next
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        slow.next = None

        # merge two linked list in order that is given in question
        first, second = head, prev
        while second:
            # tmp1, tmp2 to maintain the link in both ll
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

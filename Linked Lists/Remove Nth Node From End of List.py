# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node having value 0 and next                                                           pointer pointed to head
        temp = ListNode(0, head)
        l = temp
        r = head
        # move right pointer so that gap between l and r is equal to n
        while n > 0 and r:
            r = r.next
            n -= 1

        # increment l and r till r becomes Null, in this way l pointer will point to the node which is 1 less than nth node from end which is to be deleted
        while r:
            l = l.next
            r = r.next

        # now delete the node pointed by the next of l
        l.next = l.next.next

        return temp.next  # beacuse this points to the head

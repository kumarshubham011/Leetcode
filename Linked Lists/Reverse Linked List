# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # take two pointers prev, curr initially pointed to null and head
        # take third pointer temp which points to element which is next to head
        # while current is not null, make next of current equal to previous, then, increment prev and increment current to make it equal to next
        # repeat the above process
        prev, current = None, head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

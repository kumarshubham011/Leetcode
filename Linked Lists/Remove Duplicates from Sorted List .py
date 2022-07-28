# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        temp = head
        # run outer loop till last element
        while temp:
            while temp.next and temp.next.val == temp.val:
                # inner loop deletes the duplicate nodes
                temp.next = temp.next.next
            temp = temp.next
        return head

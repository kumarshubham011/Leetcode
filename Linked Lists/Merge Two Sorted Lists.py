# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we will make an empty node
        dummy = ListNode()
        temp = dummy

        # take a while loop which runs till one of the ll becomes null
        # compare the elements of ll and add it to the dummy node's next
        # it may happen that one ll becomes null in that case add the remaining elements of ll that is not null to the dummy node
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:  # value of ll1 maybe equal to or greater than ll2
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            # moved to last node of dummy node so that further addition could be done

        # check if any ll is not empty and append it to the dummy if yes
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        return dummy.next  # as dummy.val is zero

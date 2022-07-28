# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # adding values
            val = v1 + v2 + carry
            # val maybe greater than 10 in that case seperate carry and sum
            carry = val // 10
            val = val % 10
            temp.next = ListNode(val)

            # updating pointers
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


# METHOD 2

        # ln1 = ''
        # ln2 = ''
        # while l1:
        #     ln1 += str(l1.val)
        #     l1 = l1.next
        # while l2:
        #     ln2 += str(l2.val)
        #     l2 = l2.next
        # ln1 = int(ln1[::-1])
        # ln2 = int(ln2[::-1])
        # sm = str(ln1 + ln2)[::-1]
        # dummy = ListNode()
        # temp = dummy
        # for n in sm:
        #     temp.next= ListNode(int(n))
        #     temp = temp.next
        # return dummy.next

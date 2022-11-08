# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base condition
        if head is None or head.next is None:  # means single sorted node
            return head

        # split the list into two halves
        left = head
        right = self.getmid(head)
        temp = right.next
        right.next = None  # last node of 1st half->next node should be None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)  # merge two halves

    def getmid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        temp = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy.next

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getkth(groupPrev, k)
            if not kth:
                # if kth is None means there are not enough nodes for group
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth  # kth is now the first node of group
            groupPrev = temp

        return dummy.next

    def getkth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr

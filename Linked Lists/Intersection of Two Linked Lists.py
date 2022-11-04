# O(N) SPACE AND TIME
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset = set()
        while headA:
            hashset.add(headA)
            headA = headA.next
        while headB:
            if headB in hashset:
                return headB
            hashset.add(headB)
            headB = headB.next
        return None


# O(1) MEMORY AND O(N) TIME
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            # take two dummy nodes and iterate them over two lls, if any of them becomes null point it to the head of other ll and continue iterating till they collide,
            # either they will collide when they are both null or at the intersection of the lls.
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

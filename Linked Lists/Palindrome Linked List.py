# METHOD 1: O(N) MEMORY
# Definition for singly-linked list.
from tkinter.tix import ListNoteBook
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNoteBook]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        l, r = 0, len(lst)-1
        while l <= r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True


# METHOD 2: O(1) MEMORY


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first find the middle of the ll by taking fast and slow pointers
        fast, slow = head, head
        while fast and fast.next:  # until fast reaches the end of ll
            # move slow pointer by 1 and fast pointer by 2 steps
            fast = fast.next.next
            slow = slow.next
            # slow points to middle index

        # now reverse the ll after the middle index i.e slow pointer
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # now take a dummy node point it to the head and our prev pointer points to end of ll or we can say begining of second half of ll
        # start iterating both pointers till prev becomes null and check if both halves of the ll are equal

        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        return True

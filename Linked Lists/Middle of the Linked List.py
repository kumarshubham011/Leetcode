# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleOfList(head):
    # use fast and slow pointers
    # move slow pointer by one and fast pointer by two till fast pointer reaches out of scope of length of ll
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

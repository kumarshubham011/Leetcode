# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # we will copy the value which lies next to the node
        # then we will destro the link of the node which lies tot he next of the node and point it tothe node which lies next to the next of the node which is to be deleted
        node.val = node.next.val
        node.next = node.next.next

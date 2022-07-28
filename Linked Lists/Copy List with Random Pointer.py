from tkinter.tix import ListNoteBook
from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first make a copy of every node in ll using a dictionary and add each node to the dic
        dic = {None: None}
        # if a key is None then its value is none
        cur = head
        while cur:
            node = Node(cur.val)
            dic[cur] = node
            cur = cur.next

        # copy pointers
        cur = head
        while cur:
            node = dic[cur]
            node.next = dic[cur.next]
            node.random = dic[cur.random]
            cur = cur.next
        return dic[head]

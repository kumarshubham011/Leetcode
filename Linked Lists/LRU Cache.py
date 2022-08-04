# We will use doubly linked list for updation and deletion in cache
# In LRU cache most recently used element is on the right and least recently used element is on the left.

# We will first intialise a node class for doubly linked list and also initialise two seperate nodes for tracking most and least recently used elements in the cache.

# Getting value: we will used a dictionary with a key and values as a node. If element exists exists in cache we will return it, then remove from the ll and insert it again at rightmost part i.e MRU, if it does not exist we will return -1

# Putting value: If the values is already in dictionary we will remove it and insert it again at the rightmost part i.e MRU.
# We will also check if the length of cache exceeds capacity, if it does we will remove the element at LRU and also del it from cache

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # dict to store key value pair

        # adding nodes to track LRU and MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        # initially they will have link in between and we will insert elements between them
        self.left.next = self.right
        self.right.prev = self.left

    # remove from ll
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # insert at MRU i.e rightmost position
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        nxt.prev, prev.next = node, node

    def get(self, key: int) -> int:
        # if node already in cache return its value node and remove it-> add it to rightmost part
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already in cache, remove it from lru
        if key in self.cache:
            self.remove(self.cache[key])
        # add it to the cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if length of cache exceeds capacity , remove lru from left and add element to the MRU i.e rightmost part
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            # delete LRU from the cache
            del self.cache[LRU.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

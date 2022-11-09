class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def flatten(root):
    # base case
    if not root or not root.next:
        return root

    # recursive calls
    root.next = flatten(root.next)

    # merge
    root = merge(root, root.next)

    return root


def merge(a, b):
    temp = Node(0)
    res = temp

    while a and b:
        if a.data < b.data:
            temp.bottom = a
            a = a.bottom
        else:
            temp.bottom = b
            b = b.bottom
        temp = temp.bottom

    if a:
        temp.bottom = a
    if b:
        temp.bottom = b
    return res.bottom

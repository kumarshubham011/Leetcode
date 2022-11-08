class Solution:
    def addOne(self, head):
        # Reverse Linked list
        prev, next = None, None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev

        # Add 1 to the list

        temp = head
        while (temp.data == 9) and (temp.next != None):
            temp.data = 0
            temp = temp.next
        temp.data += 1

        # Reverse again to get original Linked list
        prev1 = None
        curr = head
        while curr:
            next1 = curr.next
            curr.next = prev1
            prev1 = curr
            curr = next1

        head = prev1
        return head

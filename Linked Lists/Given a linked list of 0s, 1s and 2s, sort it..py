# Traverse the list and count the number of 0s, 1s, and 2s. Let the counts be n1, n2, and n3 respectively.

# Traverse the list again, fill the first n1 nodes with 0, then n2 nodes with 1, and finally n3 nodes with 2.

class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # count the total no of 0,1,2 and store it in an array
        count = [0, 0, 0]
        ptr = head
        while ptr:
            count[ptr.data] += 1
            ptr = ptr.next

        # edit the linked list till total no of occurences don't become zero for each 0,1,2
        ptr = head
        c = 0
        while ptr:
            if count[c] == 0:
                c += 1
            else:
                ptr.data = c
                ptr = ptr.next
                count[c] -= 1
        return head

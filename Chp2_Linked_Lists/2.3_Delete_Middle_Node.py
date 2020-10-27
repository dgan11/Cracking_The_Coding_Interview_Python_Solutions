"""
Implement an algorithm to delete a node in the middle (i.e, any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node

Example:
Input:  the node c from the linked list                         a->b->c->d->e->f
result: nothing is returned, but the new linked list looks like a->b->   d->e->f
"""
from implementation import *

class Solution:
    def deleteMiddleNode(self, l, node):
        # Error Check
        if not l or not node:
            return
        
        # Go through the list until we find the parent of node
        cur = l.head
        while cur.next != node:
            cur = cur.next
        
        # Now just delete cur.next and return
        cur.next = cur.next.next


# Time  : O(n) worst case have to make one pass through the list 
# Space : O(1) just using a pointer


# TESTING
f = Node("F")
e = Node("E")
d = Node("D")
c = Node("C")
b = Node("B")
a = Node("A")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

l = SLinkedList()
l.head = a

# Before removing
print(l.traverse())

# After removing
s = Solution()
s.deleteMiddleNode(l, c)
print(l.traverse())

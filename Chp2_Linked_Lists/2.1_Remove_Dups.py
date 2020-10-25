"""
Write code to remove duplicates from an unsorted linked list

"""
from implementation import *

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def pushToFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def popFromFront(self):
        if self.head == None:
            return None
        out = self.head
        self.head = out.next
        out.next = None
        return out

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self.head
        seen = []
        while cur:
            seen.append(str(cur.data))
            cur = cur.next
        return print("->".join(seen))

    def removeDups(self):
        if not self.head:
            return
        cur = self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
"""

def removeDups(l):
    if not l.head:
        return l
    cur = l.head
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return l

# Where n is the size of the linked list
# Time  : O(n) - traverse the list and do O(1) node removal in place
# Space : O(1) - no additional data structres, removing dups in place



# Testing

l = SLinkedList() # a->a->c->c
l.pushToFront('c')
l.pushToFront('c')
l.pushToFront('b')
l.popFromFront()
l.pushToFront('a')
l.pushToFront('a')
l.traverse()
print(len(l))

l2 = SLinkedList()  # a->b->c
l2.pushToFront('c')
l2.pushToFront('b')
l2.pushToFront('a')

l3 = SLinkedList()  # c
l3.pushToFront('c')

l4 = SLinkedList()  # b->b
l4.pushToFront('b')
l4.pushToFront('b')


print("---- Remove Dups-----")
removeDups(l).traverse()  # a->c
removeDups(l2).traverse()  # a->b->c
removeDups(l3).traverse()  # c
removeDups(l4).traverse()  # b


"""
Tradeoffs

Linked List                           
Pros:   
- Guranteed O(1) insert and deletion from the front of the list

Cons:
- O(n) indexing and search 
- O(n) to find the length


Array
Pros:
O(1) indexing, find the length

Cons:
O(n) insert and delete in the worst case (amortized to O(1) average case)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly linked list just removing from head 
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
        print("->".join(seen))
        return

# l = SLinkedList()
# l.pushToFront('c')
# l.pushToFront('b')
# l.popFromFront()
# l.pushToFront('a')
# l.traverse()
# print(len(l))
# print("----------------")


## Singly Linked List You Remove From the Front and Back
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def popFront(self):
        if not self.head:
            print("Cant pop from the front of an empty string")
            return None
        if self.tail == self.head:
            self.tail = None
        out = self.head
        self.head = out.next
        out.next = None
        return out

    def popBack(self):
        if not self.tail:
            print("Cant pop from the back of an empty string")
            return None
        if self.tail == self.head:
            self.head = None
        out = self.tail
        self.tail = self.tail.prev
        out.prev = None
        return out

    def pushFront(self, data):
        newNode = DNode(data)
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pushBack(self, data):
        newNode = DNode(data)
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail = newNode

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
        print("->".join(seen))
    

# dl = DLinkedList()
# dl.popBack()
# dl.popFront()
# dl.pushBack('c')
# print("head: ", dl.head.data, " tail: ", dl.tail.data)
# dl.pushFront('x')
# print("head: ", dl.head.data, " tail: ", dl.tail.data)
# dl.traverse()
# dl.popFront()
# print("head: ", dl.head.data, " tail: ", dl.tail.data)
# dl.pushFront('b')
# dl.pushFront('a')
# print("head: ", dl.head.data, " tail: ", dl.tail.data)
# dl.traverse()
# print(len(dl))

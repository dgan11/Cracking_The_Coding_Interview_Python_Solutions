"""
Implement an algorithm to find the Kth to last element of a singly linked list

Assuming that the 0th to last element is the last element
"""

from implementation import *

class Solution:
    def kthToLast(self, l, k):
        # Edge Case: Passed in an empty list
        if not l:
            return None

        # Initiate the slow and fast pointers
        slow = fast = l.head

        # Move the fast pointer over k times, check that there are not K elements in l
        for i in range(k):
            fast = fast.next
            if not fast:
                return None

        # Move slow and fast incrementally until fast reaches the tail
        while fast.next: # *Most important, continue moving over until fast is at the tail - happens when no fast.next
            fast = fast.next
            slow = slow.next
        return slow

# Time  : O(n) - making in the worst case one pass through the list, best case actually dont have to go through the whole list with checks
# Space : O(1) - only using two pointers, storage doesnt grow as n does


#
#  4th 3rd  2nd  1st  0th    from last
# [1]->[2]->[3]->[4]->[5]
l = SLinkedList()
l.pushToFront(5)
l.pushToFront(4)
l.pushToFront(3)
l.pushToFront(2)
l.pushToFront(1)
l.traverse()

l2 = SLinkedList()
l2.pushToFront(0)

print("----------------")
s = Solution()
# print(s.kthToLast(l, 0).data)   # should be 5
# print(s.kthToLast(l, 2).data)   # should be 3
# print(s.kthToLast(l, 4).data)   # should be 1
# print(s.kthToLast(l, 5))        # should be none

# print(s.kthToLast(l2, 0).data)      # 0
# print(s.kthToLast(l2, 1))           # None


"""
Implement an algorithm to determine if a string has all unique charachters.
What if you cant use additional charachters?
"""

class Solution:
    def isUnique(self, s):
        d = {}
        for letter in s:
            if letter in d:
                return False
            d[letter] = 1
        return True

# Time  : O(n)
# Space : O(n)

class Solution2:
    def isUnique(self, s):
        s = sorted(s) # Sort the string and look one ahead
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        return True

# Time  : O(n logn)
# Space : O(1)

test1 = Solution()
assert(test1.isUnique('s'))
assert(test1.isUnique('asdfjkl'))
assert(test1.isUnique('ss') == False)


test2 = Solution2()
assert(test2.isUnique('s'))
assert(test2.isUnique('asdfjkl'))
assert(test2.isUnique('ss') == False)

"""
Given two strings, write a method to decide if one is a permutation
of the other
"""
# Method 1: Easy, medium speed, no extra space
# Sort the strings and see if they are the same
class Solution:
    def checkPerm(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2

# Time  : O(2 n*logn)
# Space : O(1)

# Method 2: Faster, more space
# Use a dictionary of letter counts and check against it
class Solution2:
    def checkPerm(self, s1, s2):
        d = {}
        # Loop through s1 to increment count
        for letter1 in s1:
            d[letter1] = d.get(d[letter1], 0) + 1
        # Loop through s2 to decrement count 
        for letter2 in s2:
            if letter2 not in d or d[letter2] == 0:
                return False
            d[letter2] = d[letter2]-1
        # Final check make sure only 0's in d
        for count in d.values():
            if count != 0:
                return False
        return True

# Time  : O(3 n)  where n is the length of max(s1, s2)
# Space : O(n)


test1 = Solution()
assert(test1.checkPerm('bed', 'deb'))
assert(test1.checkPerm('bed', 'debbbb') == False)
assert(test1.checkPerm('bed', 'dea') == False)

test2 = Solution()
assert(test2.checkPerm('bed', 'deb'))
assert(test2.checkPerm('bed', 'debbbb') == False)
assert(test2.checkPerm('bed', 'dea') == False)
assert(test2.checkPerm('hello', 'yellow') == False)
assert(test2.checkPerm('mellow', 'wellom'))

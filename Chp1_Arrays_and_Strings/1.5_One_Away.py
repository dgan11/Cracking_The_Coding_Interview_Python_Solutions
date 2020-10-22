"""
There are three types of edits that can be performed on strings: 
- insert a charachter
- remove a charachter
- replace a charachter

Given two strings, wrtie a function to check if they are one edit
(or zero) edits away

Ex:
pale, ple -> True    // {'a':1}
pales, pale -> True  // {'s':1}
pale, bale -> True   // {'p':1, 'b':1}
pale, bake -> False  // {'p':1, 'l':1, 'b':1, 'k':1}
ppp, app
"""

"""
How to check that zero edits
- check the strings are the same

How to check that one edits"
- If the length of one string is more than the other+1 then there has to be more than one edit

How to check for insertion/remove a charachter:
- dictionary can add and then remove, if more than one character has a count leftover than False

How to check for replace a charachter:
- 
"""


class OnePassSolution:
    def oneAway(self, s1, s2):
        s1_size = len(s1)
        s2_size = len(s2)
        if abs(s1_size - s2_size) > 1:
            return False
        elif s1_size == s2_size:
            return self.checkSwap(s1, s2)
        elif s1_size > s2_size:
            return self.checkChange(s1, s2)
        else:
            return self.checkChange(s2, s1)

    def checkSwap(self, s1, s2):
        numSwaps = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                numSwaps += 1
                if numSwaps > 1:
                    return False
        return True

    def checkChange(self, longer, shorter):
        li, si = 0, 0
        numChanges = 0
        while li < len(longer) and si < len(shorter):
            if longer[li] != shorter[si]:
                numChanges += 1
                if numChanges > 1:
                    return False
            else:
                si += 1
            li += 1
        return True

# Time  : O(2n) where n is the lenght of the shorter. O(1) if the strings are more than 1 length away.
# Space : O(1) space requirement doesn't change as n increases

test2 = OnePassSolution()
assert(test2.oneAway('pale', 'ple'))
assert(test2.oneAway('pale', 'bale'))
assert(test2.oneAway('pale', 'bale'))
assert(test2.oneAway('pale', 'bake') == False)

class Solution:
    def oneAway(self, s1, s2):
        if abs(len(s1)-len(s2)) > 1:
            return False
        if s1 == s2:
            return True

        # Local Vars 
        letterCounts = {}
        changesCount = 0

        # Insert letters from s1 into letterCounts 
        for curLetterS1 in s1:
            letterCounts[curLetterS1] = letterCounts.get(curLetterS1, 0) + 1

        # Insert letters from s2 into letterCounts
        for curLetterS2 in s2:
            if curLetterS2 in letterCounts:
                letterCounts[curLetterS2] = letterCounts[curLetterS2] - 1
            else:
                letterCounts[curLetterS2] = 1

        # Loop through counts in letterCounts
        for count in letterCounts.values():
            if count != 0:
                changesCount += 1
                if changesCount > 2:
                    return False
        return True

# Time: O(1) if string different in length or O(4n) where n is the length of the shorter
# Space: O(2n)
        
test = Solution()
assert(test.oneAway('pale', 'ple'))
assert(test.oneAway('pale', 'bale'))
assert(test.oneAway('pale', 'bale'))
assert(test.oneAway('pale', 'bake') == False)



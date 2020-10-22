"""
Given a string, write a function to check if it is a permuation of a palindrome.

A palindrome is a word or phrase that is the same forwards and backwards. 

A permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words

Example:
input: Tact Coa
output True (permutations: 'taco cat', 'atco cta')
"""

# Need to check if the string is a palindrome -- all letter counts are even except possibly 1
class Solution:
    def isPalindromePermutation(self, s):
        seenMiddleLetter = 0
        letterCounts = {}
        for letter in s.lower():
            letterCounts[letter] = letterCounts.get(letter, 0) + 1

        print(letterCounts)
        
        # Loop through and check if theres more than one letter with an odd count
        for count in letterCounts.values():
            if count % 2 == 1:
                if seenMiddleLetter:
                    return False
                seenMiddleLetter = 1
        return True


test = Solution()
print(test.isPalindromePermutation('Tact Coa'))


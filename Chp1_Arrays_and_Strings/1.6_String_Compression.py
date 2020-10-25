"""
Implement a method to perform basic string compressionusing the counts of
repeated charachters. 
Ex: 'aabcccccaaa' => 'a2b1c5a3'

If the string would not become smaller than the original, just return the original
Assume the string only has uppercase and lowercase letters
"""

class Solution:
    def compressString(self, s):
        if not s:
            return s
        i = 0
        curCount = 0
        cur = ""
        prev = ""
        out = ""

        while i < len(s):
            if i == 0:
                prev = s[i]
                cur = s[i]
                curCount = 1
            else:
                prev = cur
                cur = s[i]
                if cur == prev:
                    curCount += 1
                else:
                    out = out + prev + str(curCount)
                    curCount = 1
            i += 1
        # Add the last charachter at the end
        out = out + cur + str(curCount)
        if len(out) > len(s):
            return s
        return out

# Time  : O(n) where n is the length of the s -- have to do one pass through the string  
# Space : O(n) need to build out the output string as we go and store that


test = Solution()
print(test.compressString('aabb'))
print(test.compressString('aabbcccccaaa'))
print(test.compressString('aabbcccccb'))
print(test.compressString('a'))
print(test.compressString('ab'))

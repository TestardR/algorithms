class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        leftIdx = 0
        res = 0

        for rightIdx in range(len(s)):
            while s[rightIdx] in charSet:
                charSet.remove(s[leftIdx])
                leftIdx += 1
            charSet.add(s[rightIdx])
            res = max(res, rightIdx - leftIdx + 1)
            
        return res
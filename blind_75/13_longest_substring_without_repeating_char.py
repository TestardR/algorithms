class Solution:
    def lengthOfLongestSubstring(self, s):
        length = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = max(length, right - left + 1)
            
        return length
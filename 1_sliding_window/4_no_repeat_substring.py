class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        start = 0
        res = 0

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            res = max(res, end - start + 1)
            
        return res
    
print(Solution().lengthOfLongestSubstring("abccde"))
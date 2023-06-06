class Solution:
    def longestPalindrome(self, s):
       letterSet = set()
       
       for i in range(len(s)):
           if s[i] in letterSet:
               letterSet.remove(s[i])
           else: 
               letterSet.add(s[i])
       
       if len(letterSet) > 0:
           return len(s) - len(letterSet) + 1
       else:
           return len(s)
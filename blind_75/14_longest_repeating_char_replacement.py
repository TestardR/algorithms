class Solution:
    def characterReplacement(self, s, k):
        count = {}
        maxFreq = 0
        left = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])
            
            if (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
                
        return (right - left + 1) 
        
        
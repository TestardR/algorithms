class Solution:
    def characterReplacement(self, s, k):
        count = {}
        res = 0

        leftIdx = 0
        maxFrequency = 0
        for rightIdx in range(len(s)):
            count[s[rightIdx]] = 1 + count.get(s[rightIdx], 0)
            maxFrequency = max(maxFrequency, count[s[rightIdx]])

            if rightIdx - leftIdx + 1 - maxFrequency > k:
                count[s[rightIdx]] -= 1
                leftIdx += 1
                
            res = max(res, rightIdx - leftIdx + 1)

        return res
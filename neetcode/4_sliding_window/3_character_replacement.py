class Solution:
    def characterReplacement(self, s, k):
        count = {}
        res = 0

        start = 0
        maxFrequency = 0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            maxFrequency = max(maxFrequency, count[s[end]])

            if end - start + 1 - maxFrequency > k:
                count[s[end]] -= 1
                start += 1
                
            res = max(res, end - start + 1)

        return res
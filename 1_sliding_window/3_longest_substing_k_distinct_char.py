class Solution:
    def longestSubString(self, str, k):
        start = 0
        charMap = {}
        maxLen = 0

        for end in range(len(str)):
            charMap[str[end]] = 1 + charMap.get(str[end], 0)

            while len(charMap) > k:
                charMap[str[start]] -= 1

                if charMap[str[start]] == 0:
                    charMap.pop(str[start])

                start += 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen


print(Solution().longestSubString("araaci", 2))

# Similar to fuits into baskets

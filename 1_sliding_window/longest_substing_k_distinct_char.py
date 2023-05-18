class Solution:
    def longestSubString(self, str, k):
        start = 0
        end = 0
        char_map = dict()
        max_len = 0

        for end in range(len(str)):
            if str[end] in char_map.keys():
                char_map[str[end]] += 1
            else:
                char_map[str[end]] = 1

            while len(char_map) > k:
                char_map[str[start]] -= 1

                if char_map[str[start]] == 0:
                    char_map.pop(str[start])

                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len


# print(Solution().longestSubString("araaci", 2))

# Similar to fuits into baskets

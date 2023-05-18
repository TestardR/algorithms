class Solution:
    def lengthOfLongestSubstring(self, str):
        start = 0
        end = 0
        char_map = dict()
        max_len = 0
        
        for end in range(len(str)):
            char = str[end]
            if char_map.get(char):
                start = max(start, char_map.get(char) + 1)
                
            char_map[char] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len
    
print(Solution().lengthOfLongestSubstring("ababc"))
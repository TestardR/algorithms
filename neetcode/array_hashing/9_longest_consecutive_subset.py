class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if start of sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
                
        return longest    
                
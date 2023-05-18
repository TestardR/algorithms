import math


class Solution:
    def maxSum(self, arr, s):
        windowStart = 0
        windowEnd = 0
        windowSum = 0
        minLength = math.inf

        while windowEnd < len(arr):
            windowSum += arr[windowEnd]

            if windowSum >= s:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= arr[windowStart]
                windowStart += 1
                
            windowEnd += 1
            
        return minLength

print(Solution().maxSum([3, 4, 1, 1, 6], 8))
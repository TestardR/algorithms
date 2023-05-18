class Solution:
    def maxSum(self, arr, k):
        windowStart = 0
        windowEnd = 0
        windowSum = 0
        maxSum = 0

        while windowEnd < len(arr):
            windowSum += arr[windowEnd]

            if windowEnd >= k - 1:
                maxSum = max(maxSum, windowSum)
                windowSum -= arr[windowStart]
                windowStart += 1
                
            windowEnd += 1
            
        return maxSum

print(Solution().maxSum([2, 1, 5, 1, 3, 2], 3))
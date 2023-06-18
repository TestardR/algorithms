class Solution:
    def minSum(self, arr, s):
        start = 0
        windowSum = 0
        minLength = float("inf")

        for end in range(len(arr)):
            windowSum += arr[end]

            while windowSum >= s:
                minLength = min(minLength, end - start + 1)
                windowSum -= arr[start]
                start += 1
            
        return minLength if minLength != float("inf") else 0

print(Solution().maxSum([2, 1, 5, 2, 3, 2], 7))

# sliding window

class Solution:
    def findAverages(self, arr, k):
        result = []
        windowSum = 0
        windowStart = 0
        windowEnd = 0

        while windowEnd < len(arr):  
            windowSum += arr[windowEnd]

            if windowEnd >= k - 1:
                result.append(windowSum / k)
                windowSum -= arr[windowStart]
                windowStart+= 1

            windowEnd += 1

        return result
    
print(Solution().findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
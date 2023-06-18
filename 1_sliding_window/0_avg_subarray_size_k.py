# sliding window

class Solution:
    def findAverages(self, arr, k):
        result = []
        windowSum = 0
        start = 0

        for end in range(len(arr)):  
            windowSum += arr[end]

            if end >= k - 1:
                result.append(windowSum / k)
                windowSum -= arr[start]
                start += 1
                
        return result
    
print(Solution().findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
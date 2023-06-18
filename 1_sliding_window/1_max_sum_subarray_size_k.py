# class Solution:
#     def maxSum(self, arr, k):
#         start = 0
#         windowSum = 0
#         maxSum = 0

#         for end in range(len(arr)):
#             windowSum += arr[end]

#             if end + 1 >= k:
#                 maxSum = max(maxSum, windowSum)
#                 windowSum -= arr[start]
#                 start += 1

#         return maxSum

# print(Solution().maxSum([2, 1, 5, 1, 3, 2], 3))

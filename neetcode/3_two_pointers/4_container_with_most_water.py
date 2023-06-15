# class Solution:
#     def maxArea(self, height):
#         leftIdx = 0
#         rightIdx = len(height) - 1
#         h = max(height)
#         res = 0
        
#         while leftIdx < rightIdx:
#             res = max(res, min(height[leftIdx], height[rightIdx]) * (rightIdx - leftIdx))
#             if height[leftIdx] < height[rightIdx]:
#                 leftIdx += 1
#             elif height[rightIdx] <= height[leftIdx]:
#                 rightIdx -= 1
            
#             if h * (rightIdx - leftIdx) <= res: break
                
#         return res
    
class Solution:
    def maxArea(self, height):
        leftIdx = 0
        rightIdx = len(height) - 1
        res = 0
        
        while leftIdx < rightIdx:
            res = max(res, min(height[leftIdx], height[rightIdx]) * (rightIdx - leftIdx))
            if height[leftIdx] < height[rightIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1
                
        return res
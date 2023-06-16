class Solution:
    def trap(self, height): 
        if not height: return 0
        
        leftIdx = 0
        rightIdx = len(height) - 1
        leftMax = height[leftIdx]
        rightMax = height[rightIdx]
        
        while leftIdx < rightIdx:
            if leftMax < rightMax:
                leftIdx += 1
                leftMax = max(leftMax, height[leftIdx])
                res += leftMax - height[leftIdx]
            else:
                rightIdx -= 1
                rightMax = max(rightMax, height[rightIdx])
                res += rightMax - height[rightIdx]
                
        return res
        